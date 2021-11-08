
"""numbers = [1,10,5,16,4,9,10]
letters =['a','g','s','b','y','a','s']

#print(min(numbers))
numbers[4]=40
numbers.append(49)
numbers.insert(3,78)
numbers.insert(-1,52)
numbers.pop(-1) #index vermessen en sonudakini siler
numbers.remove(1)
numbers.sort()#listeyi sıralar
numbers.reverse()#tam tersine cevirir
print(numbers)

letters.sort()
print(letters)
print(letters.count('a'))"""


names = ['Ali','Yagmur','Hakan','Deniz']
years =[1998,2000,1998,1987]
names.append('Cenk')
names.insert(0,'Sena')
#names.remove('Deniz')
index=names.index('Deniz')
print(index)
result = 'Ali' in names
print(result)
names.reverse()
names.sort()
print(years.sort())
print(min(years))
print(max(years))
print(names)
print(years.count(1998))


#diziyi listeye cevirme
str="Chevrolet,Dacia"
result = str.split(',')
print(result)

