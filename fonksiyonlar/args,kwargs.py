# def selamla(mesaj,*args):
#     sonuc=""
#     sonuc+=mesaj
#     for arg in args:
#         sonuc+=arg
#         sonuc+=" "
#
#     return sonuc
#
# print(selamla("Merhaba ","Ali","Nasılsın?"))


def fonk(zorunlu,*args,**kwargs):
    print(zorunlu)
    for arg in args:
        print(arg)
    print("*****")

    for key,value in kwargs.items():
        print(key,value)


fonk(2,3,4,5,ad="naz",soyad="as")
        