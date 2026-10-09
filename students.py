class Students:
    list_grades=[]
    def __init__(self,name,family,nationalcode,mobile):
        self.name=name
        self.family=family
        self.nationalcode=nationalcode
        self.mobile=mobile
        self.grades=[]

    def add_grade(self,grade:float):
        self.grades=grade
        self.list_grades.append(grade)
        print(f"grade{self.list_grades}added successfully")
        
    def __str__(self):
         text=f"Name: {self.name} {self.family}\nNational Code: {self.nationalcode}\nMobile: {self.mobile}"
         return text
list_students=[]
def calculate_average():
    for item in list_students:
        if len(item.list_grades)==0:
            print(f"{item.name} {item.family} has no grades.")
        else:
            average=sum(item.list_grades)/len(item.list_grades)
            print(f"Average grade for {item.name} {item.family} is: {average}")
def register_student():
    while True:
        student=Students(
            input("Enter Name: "),
            input("Enter Family: "),
            input("Enter National Code: "),
            input("Enter Mobile: ")
        )
        list_students.append(student)
        ans=input("Do you want to continue? (y/n): ")
        if ans.lower()!='y':
            break
def add_grades():
    for item in list_students:
        print(f"enter grades for {item.name} {item.family} (type 'done' when finished):")
        while True:
            grade_input=input("Enter grade: ")
            if grade_input.lower()=='done':
                break
            grade=float(grade_input)
            item.add_grade(grade)

def show_students():
    for item in list_students:
        print(item)
        print("-------------------")
def main():
        text_menu="""
        1. New Student
        2. Add Grades
        3.show Students
        4.show average grade
        5. Exit
        please select an option:
        """

        while 1:
            get=int(input(text_menu))
            if get==1:
                register_student()
            elif get==2:
                add_grades()
            elif get==3:
                show_students()
            elif get==4:
                calculate_average()
            elif get==5:
                break
if __name__=="__main__":
    main()
           