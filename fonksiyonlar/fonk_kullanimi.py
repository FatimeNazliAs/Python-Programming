"""def sayHello(name = "user"):
    print("hello",name)

sayHello('nazli')
sayHello("melis")
sayHello()

def total(num1,num2):
    return num1+num2

print("total is",total(10,20))"""

def yasHesapla(yil):
    return 2021-yil

def emeklilik(yil,isim):
    yas=yasHesapla(yil)
    emeklilik=65-yas

    if emeklilik>0:
        print(f"emekliliginize {emeklilik} yıl kaldı.")

    else:
        print("emekli oldunuz.")

emeklilik(2001,'Fehmi')