import json 
import os 
from datetime import datetime
from typing import Any,Dict,List,Optional,Set
from pathlib import Path
import tempfile
import getpass
import base64
import hashlib
import copy
import unittest
#pip install cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    print("Cryptography library is not available Encription and decryption will not work.")
    print("To install it, run: pip install cryptography")
    CRYPTOGRAPHY_AVAILABLE = False
class ConfigManagers:
    def __init__(self,config_file:str="config.json"):
        self.config_path=config_file
        self.config = {}
        self.backup_config ={}
        self.history=[]
    def load_config(self) ->bool:
        try:
            with open(self.config_path,'r',encoding='utf-8') as file:
                self.config = json.load(file)
                self.backup_config = copy.deepcopy(self.config)
                print(f"Configuration loaded from {self.config_path}.")
                return True
        except FileNotFoundError:
            print(f"Configuration file {self.config_path} not found")
            return False
        except json.JSONDecodeError:
            print(f"error decoding json from {self.config_path}")
            return False
        except Exception as e:
            print(f"an error occurred while loading the configuration:{e}")
            return False
    def get_Value(self,path:str,default:Any =None) ->Any:
        keys=path.split('.')
        current=self.config
        for key in keys:
            if isinstance(current,dict) and key in current:
                current = current[key]
            else:
                return default
        return current
    def set_value(self,path:str,value:Any) -> bool:
        keys=path.split('.')
        current=self.config
        for i,key in enumerate(keys[:-1]):
            if key not in current:
                current[key] ={}
            elif not isinstance(current[key],dict):
                current[key] = {}
            current = current[key]
        old_value = current.get(keys[-1],None)
        current[keys[-1]] = value
        self.history.append({
            "timestamp":datetime.now().isoformat(),
            "action":"update",
            "path":path,
            "old_value":old_value,
            "new_value":value
        })
        print(f"set config{path} = {value}")
        return True
    def save_config(self,config_path:Optional[str]=None) ->bool:
        path=config_path or self.config_path
        try:
            with open(path,'w',encoding='utf-8') as file:
                json.dump(self.config,file,indent=2,ensure_ascii=False)
                self.history.append({
                    "timestamp":datetime.now().isoformat(),
                    "action":"save",
                    "path":path
                })
                print(f"save configuration is {path}")
                return True
        except Exception as e:
            print(f"Save error :{e}")
            return False
    def restore_backup(self)->bool:
        if self.backup_config:
            self.config = copy.deepcopy(self.backup_config)
            print("restore config file ...")
            return True
        print("can not finf backup file ")
        return False
    def export_for_deployment(self,environment:str)->bool:
        env_config=copy.deepcopy(self.config)
        if environment == "production":
            if "logging" in env_config:
                env_config["database"]["host"] = "prod-server.internal"
                env_config["database"]["port"] = 5432
            if "logging" in env_config:
                env_config["logging"]["level"] = "WARNING"
            if "features" in env_config:
                env_config["features"]["debug_mode"] = False
        elif environment =="development":
             if "logging" in env_config:
                 env_config["database"]["host"] = "localhost"
                 env_config["database"]["port"] = 5433
             if "logging" in env_config:
                 env_config["logging"]["level"] = "DEBUG"
             if "features" in env_config:
                 env_config["features"]["debug_mode"] = True
        elif environment =="testing":
             if "logging" in env_config:
                 env_config["database"]["host"] = "test-db"
                 env_config["database"]["port"] = 5434
             if "logging" in env_config:
                 env_config["logging"]["level"] = "INFO"
        env_file=f"config_{environment}.json"
        with open(env_file,'w',encoding="utf-8") as e_file:
            json.dump(env_config,e_file,indent=2,ensure_ascii=False)

        print(f"Save config environment {environment} in {env_file}.")
        return True
    def to_environment_varuables(self) ->Dict[str,str]:
        env_vars = {}
        def flattent(obj,prefix=''):
            if isinstance(obj,dict):
                for key , value in obj.items():
                    new_prefix=f"{prefix}{key}_" if prefix else f"{key}_"
                    flattent(value,new_prefix.upper())
            elif isinstance(obj,list):
                 env_vars[f"{prefix[:-1]}"] = json.dumps(obj)
            else:
                env_vars[prefix[:-1]] = str(obj)
        flattent(self.config)
        return env_vars
    def show_history(self,count:int=None):
        print("show history")
        print('*'*50)
        for entry in self.history[-(count) if count else 0:]:
            print(f"[{entry['timestamp']}] {entry['action']} : {entry.get('path','N/A')}")

    def validate_config(self) ->List[str]:
        errors=[]
        required_fields=["database","api_settings","logging"]
        for filed in required_fields:
            if filed not in self.config:
                errors.append(f"{filed} not in configuration it is required filed")
        if "database" in self.config:
            db_config=self.config["database"]
            if db_config.get("port",0) < 1024:
                errors.append(f"must database port than bigger on 1024")
        return errors

class SecureConfigManager(ConfigManagers):
      SENITIVE_FIELDS={
          'password','pass','pwd','secret','token','api_key','private_key',
          'access_key','secret_key','auth_token','credentials','certificate'
      }
      def __init__(self,config_file:str="config.json",key_file:str=".secret_key"):
          super().__init__(config_file)
          self.key_file=key_file
          self.fernet=None
          self.master_key=None
      def generate_master_key(self,password:str,salt:Optional[bytes]=None) ->tuple:
          if not CRYPTOGRAPHY_AVAILABLE:
            #   print("Please install cryptography with command: pip install cryptography")
            #   return
             raise ImportError("Please install cryptography with command: pip install cryptography")
          if salt is None:
              salt=os.urandom(16)
          kdf=PBKDF2HMAC(
              algorithm=hashes.SHA256(),
              length=32,
              salt=salt,
              iterations=480000
          )
          key=base64.urlsafe_b64encode(kdf.derive(password.encode()))
          return key,salt
      def initialize_encryption(self,password:Optional[str]=None) -> bool:
          if not CRYPTOGRAPHY_AVAILABLE:
              print("Please install cryptography with command: pip install cryptography")
              return False
          try:
              if os.path.exists(self.key_file):
                  print("Read key file ...")
                  with open(self.key_file,'r') as file:
                      data=json.load(file)
                      salt=base64.b64decode(data['salt'])
                      encrypted_key=base64.b64decode(data['key'])
                      if password is None:
                          password=getpass.getpass("please enter private password :")
                      key,_=self.generate_master_key(password,salt)
                      temp_frenet=Fernet(key)
                      self.master_key=temp_frenet.decrypt(encrypted_key)
                      self.fernet=Fernet(self.master_key)
                      print("Success run system encrypt...")
              else:
                  print("Create new file key ...")
                  if password is None:
                      password=getpass.getpass("please enter strong private password :")
                      confirem_password=getpass.getpass("Please enter again password:")
                      if password!=confirem_password:
                          print("Not match password")
                          return False
                  self.master_key=Fernet.generate_key()
                  self.fernet = Fernet(key)
                  key,salt=self.generate_master_key(password)
                  temp_frenet=Fernet(key)
                  encrypted_master_key=temp_frenet.encrypt(self.master_key)
                  with open(self.key_file,'w') as file:
                      json.dump({
                          'key':base64.b64encode(encrypted_master_key).decode(),
                          'salt':base64.b64encode(salt).decode(),
                          'algorithm':'PBKDF2-SAH256',
                          'iterations':480000
                      },file,indent=2)
                  os.chmod(self.key_file,0o600)
                  print('create new key file saved ...')
                  print(f'save key file in .secret_key.')
                  return True
          except Exception as e:
                 print("Error create key file:{e}")
                 return False
      def is_sensitive_field(self,name_field:str)->bool:
          field_lower=name_field.lower()
          return any(sensitive in field_lower for sensitive in self.SENITIVE_FIELDS)
      def encrypt_value(self,value:str)->str:
          if not self.fernet:
              raise ValueError("Not run encrypt system ...")
          encrypted=self.fernet.encrypt(value.encode())
          return f"ENC:{base64.b64encode(encrypted.encode())}"
      def decrpt_value(self,value_encrypt:str)->str:
          if not value_encrypt.startswith('ENC:'):
              return value_encrypt
          if not self.fernet:
              raise ValueError("Not run encrypt system ... ")
          try:
              encrypted_data = base64.b64decode(value_encrypt[4:])
              decrypted = self.fernet.decrypt(encrypted_data)
              return decrypted
          except Exception as e:
              print(f"error decrypt:{e}")
              return value_encrypt
      def encrypt_senstive_fields(self,data:dict,parent_key='')->dict:
          encrypted_data={}
          for key,value in data.items():
              full_key = f'{parent_key}.{key}' if parent_key else key
              if isinstance(value,dict):
                  encrypted_data[key]=self.encrypt_senstive_fields(value,full_key)
              elif isinstance(value,list):
                    encrypted_list=[]
                    for item in value:
                        if isinstance(item,dict):
                            encrypted_list.append(
                                self.encrypt_senstive_fields(item,f"{full_key}[]")

                            )
                        elif isinstance(item,str) and self.is_sensitive_field(key):
                            encrypted_list.append(self.encrypt_value(item))
                        else:
                            encrypted_list.append(item)
                    encrypted_data[key] = encrypted_list
              elif isinstance(value,str) and self.is_sensitive_field(key):
                   encrypted_data[key] = self.encrypt_value(value)
                   print(f"do it encrypt: {full_key}")
              else:
                  encrypted_data[key] = value
          return encrypted_data

      def decrypt_sensitive_fields(self,data:dict,parent_key:str = '') ->dict:
          decrypted_data={}
          for key,value in data.items():
              full_key = f"{parent_key}.{key}" if parent_key else key
              if isinstance(value,dict):
                  decrypted_data[key] = self.decrypt_sensitive_fields(value,full_key)
              elif isinstance(value,list):
                  decrypted_list=[]
                  for item in value:
                      if isinstance(item,dict):
                          decrypted_list.append(
                              self.decrypt_sensitive_fields(item,f"{full_key}")
                          )
                      elif isinstance(item,str) and item.startswith('ENC:'):
                          decrypted_list.append(self.decrpt_value(item))
                      else:
                          decrypted_list.append(item)
                  decrypted_data[key]=decrypted_list

              elif isinstance(value,str) and value.startswith('ENC:'):
                  decrypted_data[key] = self.decrpt_value(value)
              else:
                  decrypted_data[key] = value
          return decrypted_data
      def load_secure_config(self) -> bool:
        try:
            with open(self.config_file,encoding='utf-8') as file:
                self.config=json.load(file)
            self.original_config=copy.deepcopy(self.config)
            self.backup_config=copy.deepcopy(self.config)
            if self.fernet:
                self.config = self.decrypt_sensitive_fields(self.config)
            print(f'load secure file config of {self.config_path}')
            return True
        except Exception as e:
            print('error load config file: {e}')
            return False
      def save_secure_config(self,config_path:Optional[str]=None)->bool:
          path=config_path or self.config_path
          try:
              if self.fernet:
                  encrypted_config=self.encrypt_senstive_fields(self.config)
              else:
                  encrypted_config=self.config
              with open(path,'w',encoding='utf-8') as file:
                  json.dump(encrypted_config,file,indent=2,ensure_ascii=False)
              if os.name != 'nt':
                  os.chmod(path,0o600)
              print(f'Save secure config file in directory: {path}')
              return True
          except Exception as e:
              print(f'Error save Config File: {e}')
              return False
      def rotate_encryption_key(self,old_password:str,new_password:str)->bool:
          if not CRYPTOGRAPHY_AVAILABLE:
              print('please install cryptography library!')
              return False
          try:
              print('start rotate key')
              if not self.initialize_encryption(old_password):
                  print('Do not initialize encryption for old password')
                  return False
              if not self.load_secure_config():
                  print('can not load secure config')
                  return False
              self.master_key=Fernet.generate_key()
              self.fernet = Fernet(self.master_key)
              key,salt=self.generate_master_key(new_password)
              temp_fernet=Fernet(key)
              encrypted_master_key= temp_fernet.encrypt(self.master_key)
              if os.path.exists(self.key_file):
                  backup_key_file=f"{self.key_file}.backup_{datetime.now().strftime('%Y%M%d_%H%M%S')}"
                  os.rename(self.key_file,backup_key_file)
                  print(f'save backup key file:{backup_key_file}')
              with open(self.key_file,'w') as file:
                  json.dump({
                      'key':base64.b64encode(encrypted_master_key).decode(),
                      'salt':base64.b64encode(salt).decode(),
                      'algorithm':'PBKDF2_SHA256',
                      'iteration':480000
                  },file,indent=2)
              if os.name !='nt':
                  os.chmod(self.key_file,0o600) 
              if not self.save_secure_config():
                  print('not save secure config')
                  return False
              print(f'Do it rotate key')
              return True

          except Exception as e:
              print('Error rotate key: {e}')
              return False
      def create_env_template(self,output_path:str='.env.template') ->bool:
          try:
              template_lines=[
                  "#=============================================================#",
                  "# Environment configuration template",
                  f"Generated {datetime.now().isoformat()}",
                  "#===============================================================",
                  ""
              ]
              def extract_fields(data:dict,prefix:str=""):
                  for key,value in data.items():
                      env_key=f"{prefix}{key}".upper()
                      if isinstance(value,dict):
                          extract_fields(value,f"{env_key}_")
                      elif isinstance(value,list):
                          template_lines.append(f"#{env_key}=[list of value]")
                      elif self.is_sensitive_field(key):
                          template_lines.append(f"{env_key}=<your -{key}-here>")
                          template_lines.append(f"#this field will be encrypted")
                      else:
                          template_lines.append(f"{env_key}={value}")
              extract_fields(self.config)
              with open(output_path,'w',encoding='utf-8') as file:
                  file.write('\n'.join(template_lines))
              print(f'template file save in {output_path}')
              return True
          except Exception as e:
              print(f'error template file :{e}')
              return False
      def audit_sensitive_fields(self) ->Dict[str,Any]:
              audit_report={
                  'encrypted_fields':[],
                  'unencrypted_sensitive':[],
                  'total_fields':0,
                  'sensitive_fields':0

              }

              def audit_recursive(data:dict,path:str=""):
                  for key,value in data.items():
                      full_path=f"{path}.{key}" if path else key
                      audit_report['total_fields'] +=1
                      if self.is_sensitive_field(key):
                          audit_report["sensitive_fields"] +=1
                          if isinstance(value,str) and value.startswith('ENC:'):
                              audit_report['encrypted_fields'].append(full_path)
                          elif isinstance(value,str):
                              audit_report['unencrypted_sensitive'].append(full_path)
                      if isinstance(value,dict):
                         audit_recursive(value,full_path)
                      elif isinstance(value,list):
                          for i,item in enumerate(value):
                              if isinstance(item,dict):
                                  audit_recursive(item,f"{full_path}[{i}]")
                  audit_recursive(self.config)
                  return audit_report

              def mask_sensitive_for_display(self,data:dict)->dict:
                  masked_data={}
                  for key,value in data.items():
                      if isinstance(value,dict):
                          masked_data[key]=self.mask_sensitive_for_display(value)
                      elif isinstance(value,list):
                          masked_data[key]=[
                              self.mask_sensitive_for_display(item) if isinstance(item,dict)
                              else '***' if self.is_sensitive_field(key) else item
                              for item in value
                          ]
                      elif self.is_sensitive_field(key):
                          if isinstance(value,str) and len(value) > 8:
                              masked_data[key] = f"{value[":4"]} ... {value['-4:']}"
                          else:
                              masked_data[key] = '***'
                      else:
                          masked_data[key] = value
                  return masked_data