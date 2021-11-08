"""def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki islemler")

        func(name)
        print("fonksiyondan sonraki islemler")

    return wrapper
@my_decorator
def sayHello(name):
    print("Hello",name)

#sayHello=my_decorator(sayHello)
#sayHello()

sayHello("nazli")"""
import math
import time
def zamani_hesapla(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon " +func.__name__+" "+str(finish-start)+" saniye sürdü.")
    return inner

@zamani_hesapla
def usalma(a,b):
    print(math.pow(a,b))

@zamani_hesapla
def faktoriyel(num):
    print(math.factorial(num))


usalma(2,3)
faktoriyel(4)