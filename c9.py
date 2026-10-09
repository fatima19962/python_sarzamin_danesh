import math
class Math:
    staticmethod
    def isOdd(n):
        return n%2 !=0
    staticmethod
    def isEven(n):
        return n%2==0
    staticmethod
    def isSquere(n):
        i=0
        while i*i <=n:
            if i*i == n :return True
            i=i+1
        return False
    staticmethod
    def isPrimary(n):
        i=2
        while i <=n //2:
            if n% i ==0 :return False
            i=i+1
        return True
    staticmethod
    def isPrefect(n):
        i=1
        sum=0
        while i <= n // 2:
            if n%i==0 :sum +=i
            i=i+1
        return n == sum
n=int(input("Enter n"))
print("IS odd",Math.isOdd(n))
print("IS even",Math.isEven(n))
print("IS perfect",Math.isPrefect(n))
print("IS primary",Math.isPrimary(n))
print("IS squere",Math.isSquere(n))