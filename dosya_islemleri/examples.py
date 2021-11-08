"""with open("example.txt","a",encoding="utf-8") as file:
    file.write("Kendimi seviyorum\n")
    file.write("Her gün yeni bir başlangıç\n")

with open("example.txt","r+",encoding="utf-8") as file:
    #print(file.read())
    print(file.readline(50))
    liste=file.readlines()
    print(liste)"""

para=int(input("Ne kadar paranız var? "))
ad=input("Adınız: ")
soyad=input("Soyadınız: ")


while True:
    secim=int(input("1-Para Yatırma\n2-Para Çekme\n3-Kart İade\n"))
    if secim==1:
        yatirilan_miktar = int(input("Yatırmak istediginiz miktarı girin: "))
        para += yatirilan_miktar
        with open("atm.txt", "a", encoding="utf-8") as file:
            file.write(ad +' '+ soyad +':\n' +"para yatırdıktan sonra oluşan miktar " + str(para)+"\n")

    elif secim == 2:
        cekilen_miktar = int(input("Cekmek istediginiz miktarı girin: "))
        if (cekilen_miktar < para):
            para -= cekilen_miktar
            with open("atm.txt", "a", encoding="utf-8") as file:
                file.write("para çektikten sonra oluşan miktar: " + str(para)+"\n")

    else:
        break

























