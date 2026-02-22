#section A [Loops]
#sum of digits
'''
a=1234
b=0
while a>0:
    b=b+a%10
    a//=10
print("sum of digits:",b)

#reverse a number

a=123
b=0
while a>0:
    b=b*10+a%10
    a//=10
print("reverse number:",b)

#armstrong number
a=153
b=a
c=a
total=0
count=0
while a>0:
    count+=1
    a//=10
print(count,": count")
while b>0:
    e=b%10
    total=total+e**count
    b//=10
if c==total:
    print("Armstrong number")
else:
    print("its not armstrong number")

#fibonacci series
n=int(input("enter the fibonacci series:"))
a=0
b=1
print(a,b,end=" ")
for i in range(1,n+1):
    result=a+b
    print(result,end=" ")
    a=b
    b=i

#prime count find how many number exists
n=int(input("enter the range:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)

#fuctions
def even():
    n=int(input("enter the number:"))
    if n%2==0:
        print("its even")
    else:
        print("its odd")
even()

#7.factorial
def fact():
    n=int(input("enter the number:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
fact()
#8,9,10
def funct():
    choice=int(input("enter your choice :"))
    if choice==1:
        n=int(input("enter the 1st number:"))
        m=int(input("enter the 2nd number:"))
        l=int(input("enter the 3rd number:"))

        if n>m and n>l:
            print(f"{n} this is largest value")
        elif m>n and m>l:
            print(f"{m} this is largest value")
        elif l>m and l>n:
            print(f"{l} this is largest value")

    elif choice==2:
        n=str(input("enter the str value:"))
        vowel=['a','e','i','o','u']
        count=0
        for i in n:
            if i in vowel:
                count+=1
        print(count)
    elif choice==3:
        print("simple calculator...!")
        s=int(input("enter the 1st value:"))
        r=int(input("enter the 2nd value:"))
        print("\n1.add\n2.sub\n3.mul\n4.div\nenter the choice 1 2 3 or 4")
        c=int(input())
        t=0
        if c==1:
            t=s+r
            print("adding value:",t)
        elif c==2:
            t=s-r
            print("substract:",t)
        elif c==3:
            t=s*r
            print("multiply:",t)
        elif c==4:
            t=s/r
            print("divisible:",t)
funct()

import operation
num=int(input("enter the value:"))
print(operation.s(num))
print(operation.c(num))
'''







