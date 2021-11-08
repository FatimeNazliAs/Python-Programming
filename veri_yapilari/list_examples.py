"""def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


multiply=1
list=[1,2,3,4]
for x in list:
    multiply*=x

print("multiplication is",multiply)


list=[7,5,9,3,4,6]
max = list[0]
for i in list:
    if i>max:
        max=i

print("the max is ",max)



min=[]
for i in range(3):
    x=int(input("bir sayi giriniz: "))
    min.append(x)
print(min)

def find_min(min):
    minimum=min[0]
    for i in min:
        if i<minimum:
            minimum=i
    print("the min is ", minimum)

find_min(min)



def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyx', 'aba', '1221']))


l= [1]
if not l:
  print("List is empty")


def remove_even(list):
    for i in list:
        if i%2==0:
            continue
        else:
            print(i)
list=[2,5,77,8]
remove_even(list)

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-6:])

printValues()"""

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)





































