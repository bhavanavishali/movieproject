# print comman letter from two string

# def comman_letter():
#     s1 = input("enter the first string :")
#     s2 = input("enter the second string :")
#     ss1 = set(s1)
#     ss2 = set(s2)
#     s = ss1 & ss2
#     print('comman letter is:',s)
# comman_letter()


#Count the frequency of words appearing in a string Using Python

# def words():

#     str = input('enter the string:')
#     li = str.split()
#     d ={}
#     for i in li:
#         if i not in  d.keys():
#             d[i]=0
#         d[i] =d[i]+1
#     print(d)
# words()


#Conversion of two list into Dictionary Using Python

l1 = ['kukku','chinnu','ammu','anu']
l2 = [11,22,33,44]
l3 = dict(zip(l1,l2))
print(l3)

#find the largest element in array
from array import *
arr =array('i',[4,55,8,662,70])
max = arr[0]
for i in arr:
    if i>max:
        max=i
print(max)

import datetime

today = datetime.datetime.now()
today.strftime('%y-%m-%d')
print(today)
