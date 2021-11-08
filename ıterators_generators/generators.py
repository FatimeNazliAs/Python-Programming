#bellekte yer kaplamayan iterator,degeri liste icinde saklamamıza gerek yoksa
def cube():
    for i in range(4):
        yield i**3

#iterator=cube()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# for i in cube():
#     print(i)


liste=(i**3 for i in range(5))
print(liste)
for i in liste:
    print(i)
