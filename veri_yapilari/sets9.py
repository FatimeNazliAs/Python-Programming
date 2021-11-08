fruits ={'orange','apple','banana'}
#print(fruits[0])#indekslenemez ve sıralanamaz(sort)

for x in fruits:
    print(x)

fruits.add('cherry')
print(fruits)

fruits.update(['mango','grape','apple']) #aynı elemandan iki kere eklemez

fruits.remove('mango')

fruits.clear()
print(fruits)
