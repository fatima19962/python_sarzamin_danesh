import random
list_books=[]
list_programs=[]
'''
Docstring for school.main
Student 
teacher:[employee,teacher]
book
class room
program
----------------------------
student -> class room
teacher ->book
program -> class
----------------------------------
1)register books
2) register program
3) register class room
4)register student
5)register teacher
6) search 
7)edit
8)delete
9)exit
------------------------------------------
'''

class Person(object):
    def __init__(self,name,family,National_code,phone,birthday):
        self.__name=name
        self.__family=family
        self.__National_code=National_code
        self.__phone=phone
        self.__birthday=birthday

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getFamily(self):
        return self.__family
    def getNationalCode(self):
        return self.__National_code
    def getPhone(self):
        return self.__phone
    def getBirthday(self):
        return self.__birthday
    def setFamily(self,family):
        self.__family=family
    def setNationalCode(self,National_code):
        self.__National_code=National_code
    def setPhone(self,phone):
        self.__phone=phone
    def setBirthday(self,birthday):
        self.__birthday=birthday

    # def __str__(self):
    #     text=f"Name:{self.__name} {self.__family}"
    #     return text
'''
day1 time1 book1
day2 time2 book2
day3 time3 book3
day1{
time1:book1,
time2:book2
}
day2{
time1:book1,        
time2:book2
}
day3{
time1:book1,
time2:book2
}
-----------------------------
days    time1      time2      time3
day1     book1      book2      book3
day2     book1      book2      book3
-----------------------------
'''
class Program:
    # def __init__(self,day,time,book):
    #     pass
    __time_morning=['8:00 - 08:45','9:00 - 10:50','10:00 - 12:50','11:00-12:45']
    __time_afternoon=['18:00 - 18:45','19:00 - 20:50','20:00 - 22:50','21:00-23:45']
    def __init__(self,details:dict,type:int):
        self.__details=details
        self.__type=type
    def __str__(self):
        txt='\t \t'
        for time in self.__time_morning:
            txt +=f' {time} \t \t'
        for day in self.__details:
            get_detail=self.__details[day]
            txt +=f"\n {day} \t"
            books=''
            for time_book in get_detail:
                books += f" {get_detail[time_book]} \t \t"
            txt += f'\t {books} \n'
            # get_times=list(self.__details[day].keys())
            # times=''
            # for time in get_times:
            #     times += f"{time}"
            # txt += f'{day} | {get_times[0]}'
        return txt    
class ClassRoom:
    def __init__(self,Code,Level):
        self.__code=Code
        self.__level=Level
        self.__program=None
    def getCode(self):
        return self.__code
    def setCode(self,Code):
        self.__code=Code
    def setProgram(self,program:Program):
        self.__program=program
    def getProgram(self):
        return self.__program
class Book:
    def __init__(self,code_book,title,auther,isbn):
        self.__code=code_book
        self.__title=title
        self.__auther=auther
        self.__isbn=isbn
    def setCodeBook(self,code):
        self.__code=code
    def getCodeBook(self):
        return self.__code
    
    def setTitle(self,title):
        self.__title=title
    def getTitle(self)->str:
        return self.__title
    def setauther(self,auther):
        self.__auther=auther
    def getauther(self):
        return self.__auther
    def setisbn(self,isbn):
        self.__isbn=isbn
    def getisbn(self):
        return self.__isbn
    def __str__(self):
        txt=f"code:{self.getCodeBook()} \t Title:{self.getTitle()} Auther:{self.getauther()} ISBN:{self.getisbn()}"
        return txt
    
class Student(Person):
    def __init__(self, name, family, National_code, phone, birthday,level,student_code):
        '''
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :param family: Description
        :param National_code: Description
        :param phone: Description
        :param birthday: Description
        :param level: Description
        :param student_code: Description
        '''
        super().__init__(name, family, National_code, phone, birthday)
        self.__level=level
        self.__student_code=student_code
        self.__class=None
    def getLevel(self)->str:
        '''
        :return Description
        :rtype:str
        '''
        return self.__level
    def setLevel(self,level:str):
        self.__level=level

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getFamily(self):
        return self.__family
    def getNationalCode(self):
        return self.__National_code
    def getPhone(self):
        return self.__phone
    def getBirthday(self):
        return self.__birthday
    def setFamily(self,family):
        self.__family=family
    def setNationalCode(self,National_code):
        self.__National_code=National_code
    def setPhone(self,phone):
        self.__phone=phone
    def setBirthday(self,birthday):
        self.__birthday=birthday
    def setClass(self,Class:ClassRoom):
        self.__class=Class

    def __str__(self):
        # txt=super().__str__()
        # txt += f"Level:{self.__level}"
        
        txt=f''' Name:{super().getName()}{super().getFamily()}{super().getBirthday()}{super().getNationalCode()}{super().getPhone()} level:{self.getLevel()}'''
        return txt
# get=Student()
class Teacher(Person):
    def __init__(self, name, family, National_code, phone, birthday,CodeEMP,time,post):
        super().__init__(name, family, National_code, phone, birthday)
        self.__codeEMP=CodeEMP
        self.__time=time
        self.__post=post
        self.__books=[]
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getFamily(self):
        return self.__family
    def getNationalCode(self):
        return self.__National_code
    def getPhone(self):
        return self.__phone
    def getBirthday(self):
        return self.__birthday
    def setFamily(self,family):
        self.__family=family
    def setNationalCode(self,National_code):
        self.__National_code=National_code
    def setPhone(self,phone):
        self.__phone=phone
    def setBirthday(self,birthday):
        self.__birthday=birthday
    def getBook(self):
        return self.__books
    def setBook(self,book:Book):
        self.__books.append(book)
    def __str__(self):
        txt=f"Name:{super().getName()}{super().getFamily()}"
        return txt
    

__time_morning=['8:00 - 08:45','9:00 - 10:50','10:00 - 12:50','11:00-12:45']
dict_program={
    'Saturday':{
        __time_morning[0]:'Math',
        __time_morning[1]:'Physics',
        __time_morning[2]:'Chemistry',
        __time_morning[3]:'Biology',
    },
    'Sunday':{
        __time_morning[0]:'History',
        __time_morning[1]:'Geography',
        __time_morning[2]:'Civics',
        __time_morning[3]:'Economics',
    },
    'Monday':{
        __time_morning[0]:'Literature',
        __time_morning[1]:'Art',
        __time_morning[2]:'Music',
        __time_morning[3]:'Physical Education',
    },
}




program_test=Program(dict_program)
print(program_test)
def func_register_program():
    while 1:
        new_program=Program(
            input('enter name of program:'),
            input('enter description of program:'),
        )
        list_programs.append(new_program)
        ans=input('do you want to continue? y/n:')
        if ans=='n':
            break
        elif ans=='y':
              continue
        else:
             print(f'error: {ans}')
             break
        
def func_search_book_uni()->Book:
    book_title=input('enter title book:')
    for book in list_books:
        if book_title == book.getTitle():
            print(book)
            print('-'*10)
    code_book=input('enter code book:')
    for book in list_books:
        if code_book == book.getCode():
            return book
    return None
def func_search_book_school()->Book:
    while 1:
            book_title=input('enter title book:')
            for book in list_books:
                if book_title == book.getTitle():
                    return book
            get=input(f'can not find book with title {book_title}, do you want to try again? y/n:')
            if get.lower() =='n':
                return None
            elif get.lower() =='y':
                continue
            else:
                print('error')
                return None
            # print(book)
            # print('-'*10)
def func_details_program()->dict:
    list_days=['saturday','sunday','monday','tuesday','wednesday']
    list_zang=['zang01','zang02','zang03']
    dict_details={}
    for day in list_days:
        dict_zang={}
        for zang in list_zang:
            print( f'enter book for {day} {zang}')
            get_book=func_search_book_school()
            if get_book != None:
                dict_zang[zang]=get_book.getTitle()
            else:
                print('can not find book')
    return dict_details
def func_register_book():
    while 1:
         new_book=Book(random.randint(1000,9999),input('title:'),input('auther:'),input('isbn:'))
         if new_book.getTitle().strip() == '':
             ans=input('title is empty, do you want to try again? y/n:')
             if ans.lower() =='n':
                 break
             elif ans.lower() =='y':
                 new_book.setCodeBook(input('enter title book:'))
                 list_books.append(new_book)
             else:
                 print('error')
                 break
                 
                 
         else:
             list_books.append(new_book)
         ans=input('do you want to continue? y/n:')
         if ans=='n':
             break
         elif ans=='y':
              continue
         else:
             print(f'error: {ans}')
             break
def func_show_book():
    for book in list_books:
        print(book)

def menu_admin():
    txt_menu='''
1)register books
2) register program
3) register class room
4)register student
5)register teacher
6) search 
7)edit
8)delete
9)show
0)exit
select an option:
'''
    while 1:
        get=input(txt_menu)
        if type(eval(get)) ==int:
            if get =='1':
                func_register_book()
                print('-'*20)
            elif get =='2':
                func_register_program()
                print('-'*20)
            elif get =='3': 
                func_register_class_room()
                print('-'*20)
            elif get =='4':
                func_register_student()
                print('-'*20)
            elif get =='5':
                func_register_teacher()
                print('-'*20)
            elif get =='6':
                func_search()
                print('-'*20)
            elif get =='7':
                func_edit()
                print('-'*20)
            elif get =='8':
                func_delete()
                print('-'*20)
            elif get =='9':
                func_show_book()
                print('-'*20)
            elif get =='0':
                break
            else:
                print('select a number between 1 to 9')
        else:
            print('select a number between 1 to 9')


menu_admin()