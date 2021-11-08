def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir),end="")

def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')
    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')

    not1= int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ort=(not1+not3+not2)/3

    if ort>=90 and ort<=100:
        harf="AA"
    elif ort>=75 and ort<=89:
        harf="BB"
    elif ort>=45 and ort<=74:
        harf="CC"

    else:
        harf="FF"

    return ogrenciAdi+":"+harf +"\n"

def notlari_kayit_et():
    with open('sinav_notlari.txt',"r",encoding="utf-8") as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","a",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



def not_gir():
    ad=input('Ogrenci adı: ')
    soyad=input('Ogrenci soyadı: ')
    not1=input('not1: ')
    not2 =input('not2: ')
    not3 =input('not3: ')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+ ':'+not1+','+not2+','+not3+'\n')


while True:
    islem=input('1-Notları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n')
    if islem=='1':
        ortalamalari_oku()
    elif islem=='2':
        not_gir()

    elif islem=='3':
        notlari_kayit_et()

    else:
        break

