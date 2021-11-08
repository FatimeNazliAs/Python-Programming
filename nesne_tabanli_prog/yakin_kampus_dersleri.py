"""
class Ucus():
    havayolu="THY"
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def __repr__(self):#representation
        return f"{self.kod} sefer sayılı ucus, sistemde olusturulmustur."

    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} dakika sürecektir.".format(self.kod,self.kalkis,self.varis,self.sure)


    def koltuk_sayisi_guncelle(self):
        return self.kapasite-self.yolcu

    def bilet_satis(self,bilet_adedi=1):
        if self.yolcu+bilet_adedi<=self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print(f" {bilet_adedi} adet satılmıştır, kalan koltuk sayısı {self.koltuk_sayisi_guncelle()}")

        else:
            print("işlem geçersiz, yetersiz koltuk sayısı")


    def bilet_iptal(self,bilet_adedi=1):
        if self.yolcu>=bilet_adedi:
            self.yolcu-=bilet_adedi
            print(f" {bilet_adedi} adet iptal edilmistir, kalan koltuk sayısı {self.koltuk_sayisi_guncelle()}")

        else:
            print("işlem geçersiz, iptal edilemedi")



ucus2=Ucus('TK123','IST','ANK',60,300,50)
ucus3=Ucus('TK223','BOD','ANT',40,250,200)
print(ucus3.anons_yap())
print(ucus3.koltuk_sayisi_guncelle())
ucus3.bilet_satis(20)
ucus3.bilet_iptal(10)

#dunder methodlar(double under score)

#print(ucus3.__dir__())
print(ucus3)"""


#INHERITANCE

class Seyahat():

    def __init__(self,kalkis,varis):
        self.kalkis=kalkis
        self.varis=varis

    def anons(self):
        return f"{self.kalkis} - {self.varis} seyahatine hoşgeldiniz"


class Otobus(Seyahat):
    def __init__(self,mola_duraklari,kalkis,varis):
        Seyahat.__init__(self,kalkis,varis)
        self.mola_duraklari=mola_duraklari


s1=Seyahat('ANT','BOD')
print(s1.anons())
oto1=Otobus(['FET','ALANYA'],'IST','ANK')
print(oto1.mola_duraklari)
print(oto1.anons())


"""# Python example to show the working of multiple 
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()"""

