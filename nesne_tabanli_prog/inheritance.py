#Person=>name,lastname,age,eat(),run()
#Student(Person), Teacher()

class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print('person created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber =number
        print('student created')
    def who_am_i(self):
        print('I am a student')
    def sayHell0(self):
        print(f'Hello I am {self.studentNumber} student')



p1=Person('Ali','Yılmaz')
s1=Student('Çınar','Turan',123)

print(p1.firstName+' '+p1.lastName)
print(s1.firstName+' '+s1.lastName+' '+str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
s1.sayHell0()
p1.eat()
s1.eat()