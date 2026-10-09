def menu():
    print("1.add")
    print("2.delete")
    print("3.search")
    print("4.changeTel")
    print("5.changeName")
    print("6.printAll")
    print("7.exit")
    choose=int(input("enter your choose:"))
    return choose
def add(telbook):
    name=input("enter name")
    telno=input("enter telno")
    if name not in telbook:
        telbook[name]=telno
    else:
        print(name,"is already exist")
        print()
    return telbook
def delete(telbook):
    name=input("enter name")
    if name in telbook:
        del telbook[name]
    else:
        print(name,"not found")
    return telbook
def search(telbook):
    name=input("enter name")
    if name in telbook:
        print("telno",telbook[name])
    else:
        print(name,"not found")

def changeTel(telbook):
    name=input("enter name")
    telno=input("enter new telno")
    if name in telbook:
        telbook[name]=telno
    else:
        print(name,"not found")
    return telbook
def changeName(telbook):
    oldname=input("enter old name")
    newname=input("enter new name")
    if oldname in telbook:
        telbook[newname]=telbook.pop(oldname)
    else:
        print(oldname,"not found")
    return telbook
def printAll(telbook):
    for name in telbook:
        print(name,":",telbook[name],end='\t')
    print()
telbook={}
while 1:
    choose=menu()
    if choose==7:
        break
    elif choose==1:
        n=int(input("enter tedad:"))
        for i in range(1,n+1):
            telbook=add(telbook)
    elif choose==2:
        telbook=delete(telbook)
    elif choose==3:
        search(telbook)
    elif choose==4:
        telbook=changeTel(telbook)
    elif choose==5:
        telbook=changeName(telbook)
    elif choose==6:
        printAll(telbook)
print("-"*40)