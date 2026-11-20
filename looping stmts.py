#break
"""for i in range(0,10):
    if i==6:
        break
    print(i)"""
#continue
"""for i in range(1,8):
    if i==5:
        continue
    print(i)"""

#reverse num
"""num=12345
rev=0
while num > 0:
    digit=num%10
    rev = rev *10 + digit
    num //= 10

print(rev)"""

# rev a string
"""a="String"
rev=""
for i in range(len(a)-1,-1,-1):
    rev+=a[i]
print(rev)"""

# Missing num in th array
"""num=[1,2,3,4,5,7]
n=7
for i in range(1,n+1):
    if i not in num:
        print(i)"""

#sum of arr
"""num=[1,2,3,4,5]
sum=0
for i in num:
    sum+=i
print(sum)"""

#largest element in arr

"""num=[1,2,3,4]
largest=num[0]
for i in range(1,len(num)):
    if num[i] > largest:
        largest=i
print(largest)"""

#Rotation of an array
"""num=[1,2,3,4]
d=2
for i in range(d):
    num.append(num.pop(0))
print(num)"""

#REMAINDER OF AN ARRAY
"""num=[5,10,15]
n=5
mul=1
for i in num:
    mul*=i
print(mul%n)"""


#FACTORIAl
"""n=5
if n<0:
    print("Negative num")
else:
    f=1
    for i in range(1,n):
        f*=i+1
print(f)"""

#PRIME NUMBER
"""n=2
if n<=0:
    print("NOt a prime")
else:
    for i in range(2,n):
        if i%2==0:
            break
    else:
        print("Prime")"""

#fibonacci
"""n=10
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c"""

#given num is fibanocii or not

"""import math
n=21
def isPerfectSquare(num):
    s=int(math.sqrt(num))
    return s*s ==num
if isPerfectSquare(5*n*n + 4 ) or isPerfectSquare(5*n*n -4):
    print("fibonacii")
else:
    print("not fibonacci")""" 

#armstrong
"""a=153
num=a
sum=0
digits=len(str(num))
while a>0:
    d=a%10
    sum+=d**+digits
    a=a//10
if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong")"""

#SUM OF SQUARE OF N NUMBERS
""""
n=2
sum=0
for i in range(1,n+1):
  sum+=i*i
print(sum)
"""


#CUBE OF N NUMBERS
""""
num=int(input("Enter a number"))
sum=0
for i in range(num,num+1):
    sum+=i*i*i
print(sum)
"""

#SUM OF AN ARR
""""
arr=[1,2,3,4,5]
sum=0
for i in arr:
    sum+=i
print(sum)"""""

