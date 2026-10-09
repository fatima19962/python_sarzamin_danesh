while True:
    s=input("Enter a statement").split()
    op=s[1]
    a=int(s[0])
    b=int(s[2])
    if op in 'eEqQ' : break
    elif op in '+aA':
        c=a+b
        op='+'
    elif op in '-sS':
        c=a-b
        op='-'    
    elif op in '*mM':
        c=a*b
        op='*'
    elif op in '/dD':
        if b==0:
            print("Division by zero is not allowed.")
            continue
        c=a/b
        op='/'
    elif op in '%oO':
        if b==0:
            print("Division by zero is not allowed.")
            continue
        c=a%b
        op='%'  
    elif op in '**pP':
        c=a**b
        op='**'
    else:
        result = "Invalid operator"
        print(result)
        continue
    result="{0:d} {1:s} {2:d} {3:s} {4:6.2f}".format(a,op,b,"=",c)
    print(result)