class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def baseConverter(number,base):
    digits="0123456789ABCDEF"
    s=stack()
    while number>0:
        rem=number%base
        s.push(rem)
        number=number//base
    new_string=""
    while not s.isEmpty():
        new_string=new_string+digits[s.pop()]
    return new_string
number = int(input("enter a number"))
print('binary',baseConverter(number,2))
print('five',baseConverter(number,5))
print('binary',baseConverter(number,8))
print('headecimal',baseConverter(number,16))