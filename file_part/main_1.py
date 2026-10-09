# file=open("note.txt")
# print(file.read())
# file.close()

# text='''
# site:www
# name:sazamin
# founder:erfan
# '''
# file=open('requirement.txt','w',encoding='utf-8')
# file.write(text)
# file.write('hi\nسلام')
# file.close()


# text=b'\x00\xFF\xAA'
# file=open('requirement.bin','wb')
# file.write(text)
# file.close()


# file_list=['www','sarzamin','erfan']
# file=open('requirement.txt','w',encoding='utf-8')
# for line in file_list:
#     file.writelines(line)

# file.writelines(f'{line}\n' for line in file_list)
# file.close()
# get_write=file.write(file_list[0])
# print(get_write)
# print(file.writable())
# file.flush()
# file.close()
# if get_write>0:
#     print('success...')
# else:
#     print('can not do it command write....')








# file=open('requirement.bin','rb+')
# print(file.read())
# file.seek(-1,2)
# print(file.read())
# file.close()



file=open('requirement.txt','r+')
# print(file.tell())
# file.seek(0,2)
# position_end=file.tell()
# file.seek(position_end-4)
# print(file.tell())
# print(file.closed)
# file.close()
# print(file.closed)


# file.truncate(5)
# print(file.read())

# file.seek(5)
# file.truncate()
# file.seek(0)
# print(file.read())


# binary_buffer=file.detach()
# raw_buffer=binary_buffer.read()
# print(raw_buffer)

# import os
# file_number=file.fileno()
# file_info=os.fstat(file_number)
# print(f'size:{file_info.st_size} bytes')
# import sys

# print(sys.stdin.isatty())
# print(file.isatty())
# file.close()


# import array
# buf=bytearray(1024)
# file=open('requirement.bin','rb')
# file=open('requirement.txt','r',encoding='latin-1')
# bytes_read=file.readinto(buf)
# bytes_read=file.readinto1(buf)
# bytes_read=file.readline()
# file=reconfigure
# print(bytes_read)
# print(buf[:bytes_read])
# print(buf)
# file.close()


# with open('requirement.txt','r',encoding='utf-8') as file:
#     print(file.read())

# print('finished')



# with open('requirement.txt','r+',encoding='utf-8') as f:
#     # for line in f:
#         # print(line)

#     content=f.read()
#     f.seek(0)
#     f.write(content.upper())
#     f.truncate()




# with open('first.mp4','rb') as src, open('second.mp4','wb') as dst:
#     while chunk :=src.read(8192):
#         dst.write(chunk)



# import datetime
# with open('app.log','a',encoding='utf-8') as log:
#     log.write(f'{datetime.datetime.now()}:login superuser')
#     log.flush()


# name=input('enter a name:')
# family=input('enter a family:')
# address=input('enter a address:')
# phone=input('enter a phone:')



# with open('info_user.csv','+a',encoding='utf-8') as info:
#     # structure=f'{name},{family},{address},{phone}\n'
#     # info.write(structure)
#     # info.flush()
#     info.seek(0)
#     print(info.read())
# print('finished .....')




# def get_dat_clear(get_info:list)->list:
    
#     for line in get_info:
#         data=[]
#         line=line.split('\n')
#         data.extend(line)
#     for i in range(data.count('')):
#         data.remove('')
#     return data



# with open('info_user.csv','+a',encoding='utf-8') as info:
#     info.seek(0)
#     get_info=info.readlines()
#     new_data=get_dat_clear(get_info)
#     for item in new_data:
#         print(item)
#         item=item.split(',')
#         print(f'fullname={item[0]} {item[1]}\t address:{item[2]} \t phone:{item[3]}')





import os 
from datetime import datetime
import win32com.client as win32#pyttsx3,gTTS



class TimeCalculator:
    @staticmethod
    def subtract(time1,time2,absolute=True):
        h1,m1,s1=map(int,time1.split(":"))
        h2,m2,s2=map(int,time1.split(":"))
        second1=h1*3600 + m1*60 + s1
        second2=h2*3600 + m2*60 + s2
        diff_second = second1 - second2
        if absolute:
            diff_second=abs(diff_second)
        sign = "_" if diff_second < 0 else ""
        diff_second = abs(diff_second)
        h=diff_second // 3600
        m=(diff_second % 3600) // 60
        s= diff_second %60
        return f'{sign}{h:02d}:{m:02d}:{s:02d}'
    @staticmethod
    def add(time1,time2):
        h1,m1,s1=map(int,time1.split(":"))
        h2,m2,s2=map(int,time1.split(":"))
        total_second=((h1+h2)*3600) + ((m1+m2)*60) + (s1+s2)
        h=total_second //3600
        m=(total_second %3600) //60
        s=total_second % 60
        return f'{h:02d}:{m:02d}:{s:02d}'
    @staticmethod
    def add_list_time(times):
        seconds = 0 
        for time in times:
            h,m,s = map(int,time.split(':'))
            seconds +=(h*3600) + (m*60) + s
        h=seconds // 3600
        m=(seconds % 3600) // 60
        s=seconds % 60 
        return f'{h:02d}:{m:02d}:{s:02d}'
    @staticmethod
    def convert_to_second(time):
         h,m,s = map(int,time.split(':'))
         return (h*3600) + (m*60) + s
def save_info_employee():
    os.makedirs('database') if not os.path.isdir('database') else None
    file_path='database/employee.csv'
    check_exists=os.path.exists(file_path)
    string_header='ID,Name,Family,Phone,Post'
    number_id=1
    
    with open(file_path,'+a') as emp:
        if not check_exists:
            emp.write(f'{string_header}\n')
            emp.flush()
        else:
            emp.seek(0)
            read_data=emp.readlines()
            if len(read_data) > 1:
                # Get the last ID from the last line
                last_line = read_data[-1].strip()
                if last_line:
                    number_id = int(last_line.split(',')[0]) + 1
        
        while True:
            data_string = ''
            # Use a separate counter for the ID
            current_id = number_id
            for title in string_header.split(','):
                if title == 'ID':
                    data_string += f'{current_id},'
                else:
                    data_string += f'{input(f"please enter data for {title}:")},'
            
            # Write the data without the trailing comma
            emp.write(f'{data_string[:-1]}\n')
            emp.flush()
            
            # Increment ID for next employee
            number_id += 1
            
            ans = input('Do you want to continue (yes/no)? ')
            if ans.lower() in ['no', 'n']:
                break
                
    print('Data entry finished ...')

# save_info_employee()

def check_id_employee(id):
    with open('database/employee.csv','r') as emp:
        data=emp.readlines()
        for item in data[1:]:
            if id in item[0]:
                return True
        return False

def  get_type_io(id_emp,io):
    list_io=[]
    date=datetime.now().strftime('%Y/%m/%d')
    io.seek(0)
    # with open('database/io_employee.csv','r') as io:
    data=io.readlines()
    print(data[1:])
    print(data)
    for item in data[1:]:
        item=item.split(',')
        print(item)
        print(date)
        print(item[3])
        # if id_emp in item[0] and data in item[3]
        if id_emp  == item[1] and date == f'{item[3]}/{item[4]}/{item[5]}':
            list_io.append(item)
    if len(list_io) >0:
        if list_io[-1][2]=='i':
            return 'o'
        else:
            return 'i'
    return 'i'


def speaker_device(type:str):
    speaker=win32.Dispatch('SAPI.SpVoice')
    speaker.Speak('welcome') if type =='i' else speaker.Speak('goodbye')
def save_io_emp(id_emp):
    os.makedirs('database') if not os.path.isdir('database') else None
    file_path='database/io_employee.csv'
    check_exists=os.path.exists(file_path)
    string_header='ID,FK_ID_EMPLOYEE,Type,Year,Month,Day,Time'
    year,month,day=datetime.now().strftime('%Y/%m/%d').split('/')
    time=datetime.now().strftime('%H:%M:%S')

    number_id=1
    with open(file_path,'+a') as io:
        if not check_exists:
            io.write(f'{string_header}\n')
            io.flush()
        else:
            io.seek(0)
            read_data=io.readlines()
            if len(read_data) >1:
                number_id=int(read_data[-1][0]) + 1
        if check_id_employee(id_emp):
            type_io=get_type_io(id_emp,io)
            string_data=f'{number_id},{id_emp},{type_io},{year},{month},{day},{time}'
            io.write(f'{string_data}\n')
            io.flush()
            # if type =='i':
            #     print('welcome')
            # else:
            #     print('goodbye')
            speaker_device(type_io)

            
        else:
            print('can not found any employee...')
def get_io_emp(id_emp,year:int,month:int)->list:
    with open('database/io_employee.csv','r') as io:
        data=io.readlines()
        for item in data:
            item_list=item.split(',')
            if id_emp != item_list[1] or year !=int(item_list[3]) or month !=int(item_list[4]):
                data.remove(item)
        return data
    return []
def split_io_emp(data:list)->tuple:
    list_i=[]
    list_o=[]
    for item in data:
        item_list=item.split(',')
        if item_list[2] == 'i':
            list_i.append(item)
        else:
            list_o.append(item)
    return (list_i,list_o)
def duration_time_emp(data:tuple):
    list_i,list_o=data[0],data[1]
    list_o=list_o[:len(list_i)]


def diff_time_emp(i:list,o:list)->list:
    diff_list = []
    for t1,t2 in i,o:
        diff_list.append(TimeCalculator.subtract(t1,t2))
    return diff_list

def get_base_seconds_salary_emp(id_emp):
    with open('database/info_salary.csv','r') as info:
        data=info.readlines()
        for item in data[1:]:
            item=item.split(',')
            if id_emp == item[1]:
                return int(item[2])
    return 0
def generate_salary(id_emp,year:int,month:int)->int:
    salary=0
    list_io = get_io_emp(id_emp,2026,6)
    split_io=split_io_emp(list_io)
    list_diff = diff_time_emp(list_io[0],split_io[1])
    time_finally = TimeCalculator.add_list_time(list_diff)
    salary=get_base_seconds_salary_emp(id_emp) * TimeCalculator.convert_to_second(time_finally)
    return salary
# save_io_emp('2')