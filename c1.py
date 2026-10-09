def pow(x,n):
    p=1
    for i in range(1,n+1):
        p=p*x
    return p
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def menu():
    print("1. calculate one")
    print("2. calculate two")
    print("3. calculate three")
    print("4. Exit")
    sel = int(input("Enter your choice: "))
    return sel
def sum1(x,n):
    sum=0
    for i in range(1,n+1,1):
        sum =sum+ (pow(x,i)*pow(i,x)*pow(x,n))/(factorial(x)*factorial(n)*factorial(n+2))
        sum=sum*pow(x,n)*pow(n,5)*pow(x,x+2)/(factorial(x)+factorial(n)*factorial(x+n))
        return sum
def sum2(x,n):
    sum=0
    sign=1
    for i in range(1,n+1,1):
        sum=sum+pow(x,i)/factorial(i)*sign
        sign=-sign
        return sum
def sum3(x,n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+(pow(x,i)*pow(i,x)*pow(x,n))/(factorial(x+i)+factorial(n+x))
        sum=sum*(pow(pow(x,n),3)*pow(n,x+3))/(factorial(x)+factorial(x+n+2))
        return sum
sum=0
while 1:
    sel=menu()
    if sel==4:
        break
    x=int(input("Enter x: "))
    n=int(input("Enter n: "))
    if sel==1:
        sum=sum1(x,n)
        print("Sum 1 is: ", sum)
    elif sel==2:
        sum=sum2(x,n)
        print("Sum 2 is: ", sum)
    elif sel==3:
        sum=sum3(x,n)
        print("Sum 3 is: ", sum)
    else:
        print("Invalid choice, please try again.")