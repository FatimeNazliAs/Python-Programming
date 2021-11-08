def para_guncelle(para):
    x=para
    return x



def para_cek(para):
    cekilen_miktar = int(input("Cekmek istediginiz miktarı girin: "))
    if (cekilen_miktar < para):
        para -= cekilen_miktar
        para_guncelle(para)
        print(f"Kalan paranız: {para}")

    else:
        print("İstediginiz miktarda cekilecek paranız yok.")



def para_yatir(para):
    yatirilan_miktar = int(input("Yatırmak istediginiz miktarı girin: "))
    para+= yatirilan_miktar

    print(f"Yeni paranız: {para}")
    para_guncelle(para)



def kart_bilgileri(isim_soyisim,kart_no):

    print(f"Adınız ve Soyadınız: {isim_soyisim}\nPara: {para_guncelle()}\nKart Numarası: {kart_no}")

para=int(input("Sahip olduğunuz para miktarını girin: "))
isim_soyisim=input("İsminiz ve Soyisimiz: ")
kart_no=input("Kart Numarası: ")

"""hesap={
    'ad_soyad':isim_soyisim,
    'Kart Bilgisi':kart_no,
    'Miktar':para
}"""


while True:

    secim=int(input("1-Para Çekme\n2-Para Yatırma\n3-Kart Bilgileri\n4-Kart İade\n"))
    
    if secim==1:
        para_cek(para)

        
    elif secim==2:
        para_yatir(para)

    elif secim==3:

        kart_bilgileri(isim_soyisim,kart_no)

    else:
        print("İslem bitmiştir.")
        break

