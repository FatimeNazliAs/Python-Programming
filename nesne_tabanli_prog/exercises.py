"""class Takim():

    def __init__(self,sure,para,kisi_sayisi):
        self.sure=sure
        self.para=para
        self.kisi_sayisi=kisi_sayisi

    def haftalik_sure(self):

        if self.sure>40:
            return f"{self.sure} saat yeterli"
        else:
            return f"{self.sure} saat yeterli değil"

    def para_ihtiyaci(self):
        miktar=1000
        if self.para>=miktar:
            print("para yeterli")
        else:
            print("para yetersiz")

    def kisi(self):
        if self.kisi_sayisi>30:
            print("kisi cok fazla")
        else:
            print("kisi az")



t1=Takim(45,500,40)
print(t1.haftalik_sure())
t1.para_ihtiyaci()
t1.kisi()

class Yazilim(Takim):
    def __init__(self,para,tur):
        Takim.__init__(self,sure=2,para=100,kisi_sayisi=25)
        self.tur=tur

    def turu_nedir(self):
        print("Hangi yazılım dilini kullanıyorsunuz ? ")
        if self.tur=='python':
            print("dogru dil")
        else:
            print("yanlis dil")


y1=Yazilim(10000,'python')
y1.para_ihtiyaci()
y1.kisi()
y1.turu_nedir()"""


class Teknoloji():
    ekran = 'dokunmatik'
    def __init__(self,kulaklik):

        self.kulaklik=kulaklik



    def ne_kadar_sarj(self):
        x=int(input("Şarjınız ne kadar süre gidiyor? "))
        return f" {x} saat süre kullanabiliyorum ve ekran {self.ekran}"

    def kulaklik_girisi(self):
        if self.kulaklik=='e':
            return f" kulaklik girisi var"
        else:
            "kulaklik girisi yok"


#t1=Teknoloji('e')
#print(t1.ne_kadar_sarj())
#print(t1.kulaklik_girisi())

class Telefon(Teknoloji):
    def __init__(self,mesaj,kulaklik):
        Teknoloji.__init__(self,kulaklik)
        self.mesaj=mesaj

    def kac_mesaj(self):
        x=int(input("Gunde kaç mesaj yazıyorsunuz? "))
        if self.mesaj > x:
            return "mesaj yeterli"
        else:
            return "yeterli degil"


tel1=Telefon(100,'h')
print(tel1.kac_mesaj())

