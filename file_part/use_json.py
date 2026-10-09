import json
# data={
#     'name':'erfan',
#     'family':'mahigir',
#     'name2':'فاطمه',
#     'phone':'0912',
#     'skills':[
#         'python','sql','AI','Web'
#     ],
#     'is_active':True
# }
# json_string = json.dumps(data,ensure_ascii=False,indent=4)
# # print(json_string)
# with open('user_data.json','w',encoding='utf-8') as file:
#     # file.write()
#     json.dump(data,file,ensure_ascii=False,indent=4)
#     print('finished ...')
# with open('user_data.json','r',encoding='utf-8') as file:
#      loaded_data=json.load(file)

# print(loaded_data['skills'])
import requests
# pip install request
response = requests.get('https://api.github.com/users/python')
data=response.json()

print(f'name:{data['name']}')
print(f'bio:{data['bio']}')