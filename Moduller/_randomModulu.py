import random

"""result=dir(random)
print(result)
result=random.random() #0.0-1.0
result=random.uniform(10,100)
result=int(random.uniform(10,100))
result=random.randint(1,10)
print(result)

names=['ali','yagmur','deniz','cenk']
#result=names[random.randint(0,len(names)-1)]
result=random.choice(names)
print(result)

greeting='hello there'
result=random.choice(greeting)
print(result)"""

liste=list(range(10))
random.shuffle(liste) #elemanları karıstırır
print(liste)

liste=range(100)
result=random.sample(liste,3)
print(result)

