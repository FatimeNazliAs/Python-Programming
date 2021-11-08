#key-value

"""#dictionary yerine liste kullanılırsa
sehirler =['kocaeli','istanbul']
plakalar =[41,34]
print(plakalar[sehirler.index('istanbul')])


plakalar = {'kocaeli':41, 'istanbul':34}

plakalar['ankara']=6
plakalar['kocaeli']=40
print(plakalar)"""


"""users ={
    'nazli': {
    'age':20,
    'email':'nazli@gmail.com',
    'adress':'mersin',
    'phone':'123456'
},
  'melis': {
    'age':5,
    'email':'melis@gmail.com',
    'adress':'antalya',
    'phone':'123456'
},


}
print(users['nazli'])
print(users['melis']['age'])"""


ogrenciler={}

number =input("ogrenci no: ")
name =input("ogrenci adı: ")
surname=input("ogrenci soyadi: ")
phone=input("ogrenci telefon: ")

ogrenciler[number] = {
    'ad':name,
    'soyad':surname,
    'telefon': phone
}
print(ogrenciler)

