"""
class Person:
    #attributes
    #methods

    #class attributes
    adress='no information'

    #constructor (yapıcı metot)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year = year
    #instance methods
    def intro(self):
        print('Hello There. I am '+self.name)

    def calculateAge(self):
        return 2021-self.year

#object(instance)
p1=Person(name='ali',year=1990)
p2=Person(name='yagmur',year=1995)

#uptading
p1.adress='kocaeli'


print(p1)
print(p2)
print(type(p1))
p1.intro()
p2.intro()
print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')"""


class Circle:
    #class object attribute
    pi=3.14
    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    #Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)


c1=Circle()
c2=Circle(5)

print(f'c1: alan={c1.alan_hesapla()} çevre={c1.cevre_hesapla()}')
print(f'c2: alan={c2.alan_hesapla()} çevre={c2.cevre_hesapla()}')