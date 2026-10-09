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
        return self.time_work*self.basic_salary_hour
    def __str__(self):
         text=f"Name: {self.name} {self.family}\nNational Code: {self.nationalcode}\nMobile: {self.mobile}\nTime Work: {self.time_work} hours\nSalary: {self.salary()} IRR"
         return text
    



list_employee=[]
def register_employee():
    while True:
        employee=Employee(
            input("Enter Name: "),
            input("Enter Family: "),
            input("Enter National Code: "),
            input("Enter Mobile: ")
        )
        list_employee.append(employee)
        ans=input("Do you want to continue? (y/n): ")
        if ans.lower()!='y':
            break

def set_durations():
    for item in list_employee:
        print(f"enter duration time work for {item.name} {item.family}:")
        get_time=float(input("Enter hours: "))
        item.set_time_work(get_time)
def show_salary():
    for item in list_employee:
        print(item)
        print("-------------------")
def main():
        text_menu="""
        1. New Employee
        2. Set Time Work
        3.show salary
        4. Exit
        please select an option:
        """

        while 1:
            get=int(input(text_menu))
            if get==1:
                register_employee()
            elif get==2:
                set_durations()
            elif get==3:
                show_salary()
            elif get==4:
                break


if __name__=="__main__":
    main()
