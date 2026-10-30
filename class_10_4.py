list_employees=[]
class Employee:
    basic_salary_hour=250000
    def __init__(self,name,family,nationalcode,mobile):
        self.name=name
        self.family=family
        self.nationalcode=nationalcode
        self.mobile=mobile
        self.time_work=0
    def set_time_work(self,time:float):
        self.time_work=time
    def salary(self):
        return self.time_work * self.basic_salary_hour
    def __str__(self):
        text=f'''Name and family :{self.name}{self.family}\t natinalcode {self.nationalcode} duration work (hour) {self.time_work} \t salary {self.salary()}'''
        return text

def register_employee():
    while True:
         employee = Employee(
             input("Enter name:"),
             input("Enter family"),
             input("Enter Nationalcode"),
             input("Enter mobile")
         )
         list_employees.append(employee)
         ans=input('do you want continue (y/n) ?')
        #  if ans == 'n':
        #      break
         if ans.lower()!='y':
                    break

def set_durations():
    for item in list_employees:
        print(f'enter duration time for {item.name} {item.family}')
        get_time=float(input('enter time duration :'))
        item.set_time_work(get_time)

def show_salary():
    for item in list_employees:
        print(item)
def main():
    text_menu = '''1)New Employee
    2)set Duration Time
    3)show salary
    4)Exit
    please select option'''
    while 1:
        get=int(input(text_menu))
        if get ==1:
            register_employee()
        elif get ==2:
            set_durations()

        elif get==3:
            show_salary()

        elif get ==4:
            break

if __name__=='__main__':
     main()