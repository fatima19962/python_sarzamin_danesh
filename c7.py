def addBinarynums(x,y):
    maxlen=max(len(x),len(y))
    x=x.zfill(maxlen)
    y=y.zfill(maxlen)
    result=""
    carry=0
    for i in range(maxlen-1,-1,-1):
        r=carry
        r+=1 if x[i]=='1' else 0
        r+=1 if y[i]=='1' else 0
        result=('1' if r%2==1 else '0')+result
        carry=0 if r<2 else 1
    if carry !=0 :result = '1' + result
    return result.zfill(maxlen)
x=input("Enter first binary number: ")
y=input("Enter second binary number: ")
z=addBinarynums(x,y)
print(x.zfill(len(z)),'\n',y.zfill(len(z)),'\n','-'*60,'\n',z)