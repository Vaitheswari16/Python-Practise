# INTERCHANGING 1st ELEMENT AND 2nd ELEMENT IN THE LIST
"""num=[1,2,3,4]
temp=num[0]
num[0]=num[1]
num[1]=temp
print(num)"""

#check num is present on the list
"""list=[1,2,4,5]
n=5
for i in range(1,n+1):
    if i not in list:
        print(i)"""

#SUM OF ELEMENT IN A LIST
"""""
list=[1,2,3,4,5]
sum=0
for i in list:
    sum+=i
print(list)"""

#SMALLEST ELEMENT IN THE LIST
"""""
list=[1,2,3,4]
temp=list[0]
for i in range(1,len(list)):
    if list[i] < temp:
        temp=list[i]
print(temp)
"""
#EVEN NUM IN A LIST
"""
list=[1,2,3,4,5,6]
for i in list:
    if i%2==0:
        print(i)
        """
#USING RANGE
"""
list=[1,2,3,4,5,6]
for i in range(2,len(list)):
    if i%2==0:
        print(i)"""

#REMOVE AN ELEMENT IN A LIST
""""
list=[1,2,3,4,5]
remove=[1,4]
res=[]
for i in list:
    if i not in remove:
        res.append(i)
print(res)"""

#   occurance of elements in list
""""
list=[1,2,2,2,3,4,5,5,5,6]
count=0
for i in list:
    if i==3:
        count+=1
print(count)"""

#Remove empty tuples in a list
"""""
list=[1,2,3,(),5,6]
res=[]
for i in list:
    if i:
        res.append(i)
print(res)
"""

#break the list into chunks of n
"""""
list=[1,2,3,4,5,6,7,8,9]
n=3
for i in range(0,len(list),n):
    print(list[i:i+n])"""

#SORT THE LIST BY USING 1ST LIST
"""
import pandas as pd
a=['b','a','d','c']
b=[3,1,4,2]
df=pd.DataFrame({'a':a,'b':b})
res=df.sort_values('b')['a'].to_list()
print(res)
"""
#ADD 2 MATRIX IN THE LIST 
""""
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[10,11,12],[13,14,15],[16,17,18]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]+b[i][j]
for r in res:
    print(r)"""

#PALINDROME OR NOT
"""
a="madam"
res=""
for i in range(len(a)-1,-1,-1):
    res+=a[i]
if res==a:
    print("Palindrome")
else:
    print("Not a plaindrome")"""

#REVERSE THE WORDS IN THE STRING
""""
s="Hi Hello and welcome"
res=""
words=s.split()
for i in range(len(words)-1,-1,-1):
    res+=words[i]
print(res.strip())
"""

#LENGTH OF THE STRING
"""""
s="String"
count=0
for i in s:
    count+=1
print(count)"""

#even words in the string
""""
a="Hi Hello and welcome"
res=""
words=a.split()
for i in words:
    if len(i)%2==0:
        res+=i + " "
print(res.strip())"""

#2ND LARGEST ELEMENT IN A LIS
"""""
num=[50,30,60,100]
largest=num[0]
second_largest=None
for i in num:
    if i> largest:
        second_largest=largest
        largest=i
    elif second_largest is None or i > second_largest:
        second_largest=i
print(second_largest)
"""""

#Vowels in a string
s="hello"
count=0
for char in s:
    if char.lower() in "aeiou":
        count+=1
print(count)

#count words in the string
s="hello world"
count=0
for i in s.split():
    count+=1
    
print(count)