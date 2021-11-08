#DYNAMIC
# l=[1,2,3]
# m=[1,2,3]
# print(l==m)
# print(l is m)
# print(id(l))
# print(id(m))#identity

# a=[1,2,3]
# b=a
# print(b is a)
# b=list(a)
# print(b is a)

#LOOPS
# for x in range(10):
#     print(x)
# names=["aa","bb","cc"]
# for name in names:
#     print(name)

# age={'jim':31,'zick':32,'pam':'27','sam':35 }
# for name in age.keys():
#     print(name,age[name])
# print("\n")
# for name in age:
#     print(name,age[name])
#
# print("\n")
# for name in sorted(age,reverse=True):
#     print(name,age[name])

# numbers=range(10)
# squares=[]
# for number in numbers:
#     square=number**2
#     squares.append(square)
# print(squares)
# squares2=[number**2 for number in numbers]
# print(squares)


#FUNCTIONS
# def add(a,b):
#     mysum=a+b
#     return mysum
#
# x=add(12,15)
# print(x)
#
# newadd=add
# print(newadd(2,5))
#
# def modify(mylist):
#     mylist[0] *= 10
#     return(mylist)
# L = [1, 3, 5, 7, 9]
# M = modify(L)
# print(M is L)

# def intersect(s1,s2):
#     res=[]
#     for x in s1:
#         if x in s2:
#             res.append(x)
#
#     return res
#
# print(intersect([1,2,3,4,5],[3,4,5,6,7]))

import random

print(password(10))





