import time

# def zaman_hesapla(func):
#     def wrapper(*args,**kwargs):
#         baslangic=time.time()
#         func(*args,**kwargs)
#         bitis=time.time()
#         print(f"islem {bitis-baslangic} saniye sürdü.")
#
#     return wrapper
#
#
#
#
# @zaman_hesapla
# def kareleri_al(liste):
#     for i in liste:
#         print(i*i)
#
# @zaman_hesapla
# def kupleri_al(liste):
#     for i in liste:
#         print(i ** 3)
# @zaman_hesapla
# def topla(a,b):
#     time.sleep(1)
#     print(a+b)
#
#
# #kareleri_al(range(10000))
#
# topla(10,20)

# def zaman_hesapla(func):
#     def wrapper(*args, **kwargs):
#         baslangic = time.time()
#         sonuc=func(*args, **kwargs)
#         bitis = time.time()
#         print(f"islem {bitis-baslangic} saniye sürdü.")
#         return sonuc
#
#     return wrapper
#
#
#
# @zaman_hesapla
# def kareleri_al(liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(i*i)
#     return sonuc
#
#
# @zaman_hesapla
# def kupleri_al(liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(i**3)
#     return sonuc
#
# @zaman_hesapla
# def topla(*args):
#     time.sleep(1)
#     return sum(args)
#
#
# print(kareleri_al(range(20)))


def decorator(fonk):
    def wrapper(*args):
        print("Merhaba ben Nazli")
        fonk(*args)
    return wrapper


def kac_yasinda(yas):
    print(f"{yas} yaşındayım.")
@decorator
def meslegi_ne(meslek):
    print(f"benim meslegim {meslek}")

yasiniz=decorator(kac_yasinda)
yasiniz(20)
#kac_yasinda(20)
meslegi_ne("öğrenci")