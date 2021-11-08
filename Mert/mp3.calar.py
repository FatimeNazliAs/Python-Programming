class Sarki():
    def __init__(self,sarkilar=[]):
        self.liste=sarkilar
        self.suanCalanSarki=""
        self.ses=100
        self.durum=True

    def sarkisec(self):
        x = 0
        for i in self.liste:
            print(f"{x}. {i}")
            x += 1

        secim = int(input("istediginiz sarkının numarasını giriniz "))
        print("Sectiginiz Sarki:", self.liste[secim])
        self.suanCalanSarki = self.liste[secim]

    def sarkiEkle(self):
        sanatci=input("Sanatcıyı/Grubu giriniz: ")
        sarki=input("Sarkiyi giriniz: ")
        self.liste.append(sanatci+" - "+sarki)


    def sarkisil(self):
        x=0
        for i in self.liste:
            print(f"{x}. {i}")
            x+=1
        a = int(input("silmek istediginiz sarkının numarasını yazınız "))
        del self.liste[a]
        # self.liste.pop(a)


    def rastgeleSarkiSec(self):
        import random
        x=random.randint(0,len(self.liste))
        print("random olarak secilen sarkı",self.liste[x])
        self.suanCalanSarki = self.liste[x]



    def sesArttir(self):
        x=int(input(f"ses seviyesi: {self.ses} Ne kadar arttırmak istiyorsunuz? "))
        self.ses+=x


    def sesAzalt(self):
        x = int(input(f"ses seviyesi: {self.ses} Ne kadar azaltmak istiyorsunuz? "))
        self.ses -= x


    def kapa(self):
        self.durum=False

    def menuGoster(self):
        print("""
---Mp3 Çalara Hos Geldiniz---
Şarkı Listesi: {}
Suan Çalan Şarkı: {}
Ses Düzeyi: {}
1-Sarki sec\n2-Ses arttir\n3-Ses azalt\n4-Rastgele sarki sec\n5-Sarki ekle\n6-Sarki sil\n7-Kapat""".format(self.liste,self.suanCalanSarki,self.ses))


    def Secim(self):
        secim=int(input("Seciminizi Giriniz: "))
        while secim<1 or secim>7:
            secim=int(input("Sectiginiz deger yanlış, lutfen belirtilen aralıklarda değer giriniz. "))

        return secim


    def calistir(self):
        self.menuGoster()
        secim=self.Secim()

        if secim == 1:
            self.sarkisec()

        elif secim == 2:
            self.sesArttir()

        elif secim == 3:
            self.sesAzalt()
        elif secim == 4:
            self.rastgeleSarkiSec()

        elif secim == 5:
            self.sarkiEkle()

        elif secim == 6:
            self.sarkisil()

        elif secim == 7:
            self.kapa()

s1=Sarki()
while s1.durum:
    s1.calistir()
print("Program sonlandı.")












