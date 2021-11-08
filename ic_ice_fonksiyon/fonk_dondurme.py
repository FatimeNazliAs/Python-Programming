# def usalma(num):
#     def inner(power):
#         return num**power
#
#     return inner
#
#
# two=usalma(2)
# print(two(3))


"""def yetki_sorgula(page):
    def inner(role):
        if role=='Admin':
            return "{} rolü {} sayfasına ulaşabilir.".format(role,page)

        else:
            return "{} rolü {} sayfasına ulaşamaz.".format(role, page)

    return inner

user1=yetki_sorgula("Product Edit")
print(user1("user"))"""









def kisi_sec(kisi):
    def takim_sec(takim):
        return f"{kisi} {takim} takimini tutuyor."
    return takim_sec

a=kisi_sec("ali")
b=kisi_sec("melih")

print(a("fb"))
print(b)

















"""#fonksiyonu referans olarak gönderme

def toplama(a,b):
    return a+b
def cikarma (a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi=="toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))

    elif islem_adi == "carpma":
        print(f3(3, 4))

    elif islem_adi == "bolme":
        print(f4(10,2))

    else:
        print("geçersiz işlem...")

islem(toplama,cikarma,carpma,bolme,"toplama")
islem(toplama,cikarma,carpma,bolme,"carpma")"""