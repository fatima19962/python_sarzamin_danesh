class square:
    __x=0
    def __init__(self,x):
        self.set_x(x)
    def __del__(self):
        print("object deleted")
    def set_x(self,x):self.__x = x if x >=0 else 0
    def get_x(self,x):return self.__x   
    def __Area(self):
        return self.__x**2
    def __Prime(self):
        return 4*self.__x
    def __str__(self):
        s="X:"+str(self.__x)
        s +="\t\t Area:" + str(self.__Area())
        s +="\t\t perime:" + str(self.__Prime())
        return s
x=int(input("ENter x"))
s=square(x)
print(str(s))
del s