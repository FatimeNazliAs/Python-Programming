"""for item in range(5,100,10):
    print(item)

print(list(range(5,100,10)))


greeting ='Hello There'
for index,item in enumerate(greeting):
    print(f'index: {index} letter: {item}')


list1=[1,2,3,4,5]
list2 =['a','b','c','d','e']
list3 =[100,200,300,400,500]
print(list(zip(list1,list2,list3)))


for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(c)


numbers =[x for x in range(10)]
print(numbers)

numbers =[x*x for x in range(10) if x%3==0]
print(numbers)


myString ='Hello'
myList =[]

for letter in myString:
    myList.append(letter)

print(myList)

myList=[letter for letter in myString]
print(myList)


years =[1983,1999,2008,1956,1986]
ages=[2019-year for year in years]
print(ages)


results =[x if x%2==0 else 'tek' for x in range(1,10)]
print(results)

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers =[(x,y) for x in range(3) for y in range(3)]
print(numbers)"""



asalmi=True

for y in range(20):
    if y == 0:
        print("0 sayısı asal değildir.")
        continue

    if y == 1:
        print("1 sayısı asal değidir.")
        continue

    for i in range(2,y):


        if (y % i == 0):
            asalmi = False
            break

    if asalmi:
        print(f"{y} asal sayidir")

    else:
        print(f"{y} asal sayi degildir")

    asalmi = True