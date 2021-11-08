"""Write a Python function to find the Max of three numbers.
def find_max(x,y,z):
    if x>z and x>y:
        max=x
    elif y>z and y>x:
        max=y

    else:
        max=z

    return max

x=int(input("bir sayi giriniz: "))
y=int(input("bir sayi giriniz: "))
z=int(input("bir sayi giriniz: "))

maximum=find_max(x,y,z)
print(f"the max of three numbers is {maximum}")

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

liste = []
for i in range(4):

    a=int(input("bir sayı giriniz: "))
    liste.append(a)

print(liste)

def sum(liste):
    total = 0
    for i in liste:
        total+=i

    print(f"total is {total}")

sum(liste)


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index-= 1
    return rstr1
print(string_reverse('1234abcd'))



def find_palindrome(str):
    x=len(str)
    i=0
    a=0
    while i<=(x/2):
        if str[i]!=str[x-1]:
            a=1
            break
        else:
            a=0
        i+=1
        x-=1

    if a==0:
        print(f" {str} is palindrome")
    else:
        print(f" {str} is not palindrome")

find_palindrome('12321')

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))"""




