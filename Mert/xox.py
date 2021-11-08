class Oyun:
    def __init__(self):
        self.tahta =[[" "," "," "],[" "," "," "],[" "," "," "]]
        self.durum=True
        self.hamle=0

    def oyna(self):
        if self.hamle%2==0:
            self.p1secim()
        else:
            self.p2secim()

        self.durum=self.oyunKontrol()
        if not self.durum:
            self.tahtaGoster()
            kazanan=""
            if self.hamle%2==0:
                kazanan="X"
            else:
                kazanan = "O"

            print("Oyun sonlandı, Kazanan: {}".format(kazanan))
        self.hamle+=1



    def p1secim(self):
        self.tahtaGoster()
        print("Birinci Oyuncu")
        satir=int(input("Satiri giriniz: "))
        while satir<1 or satir>3:
            satir=int(input("Girilecek satir degeri 1,2,3 olabilir,tekrar giriniz."))
        sutun=int(input("Sütunu giriniz: "))
        while sutun < 1 or sutun > 3:
            sutun = int(input("Girilecek sütun degeri 1,2,3 olabilir,tekrar giriniz."))

        if self.doluMu(satir,sutun):
            self.p1secim()
        else:
            self.tahta[satir-1][sutun-1]="X"




    def p2secim(self):
        self.tahtaGoster()
        print("İkinci Oyuncu")
        satir = int(input("Satiri giriniz: "))
        while satir < 1 or satir > 3:
            satir = int(input("Girilecek satir degeri 1,2,3 olabilir,tekrar giriniz."))
        sutun = int(input("Sütunu giriniz: "))
        while sutun < 1 or sutun > 3:
            sutun = int(input("Girilecek sütun degeri 1,2,3 olabilir,tekrar giriniz."))

        if self.doluMu(satir, sutun):
            self.p2secim()
        else:
            self.tahta[satir-1][sutun-1] = "O"

    def doluMu(self,satir,sutun):
        if self.tahta[satir-1][sutun-1]!=" ":
            return True
        else:
            return False


        pass
    def tahtaGoster(self):
        for i in self.tahta:
            print(i)





    def oyunKontrol(self):
        # yatay kontrol
        if [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]==["X","X","X"] or [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]==["O","O","O"]:
            return False

        if [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]==["X","X","X"] or [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]==["O","O","O"]:
            return False

        if [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]]==["X","X","X"] or [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]]==["O","O","O"]:
            return False

        # dikey kontrol
        if [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]]==["X","X","X"] or [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]]==["O","O","O"]:
            return False
        if [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]]==["X","X","X"] or [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]]==["O","O","O"]:
            return False
        if [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]]==["X","X","X"] or [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]]==["O","O","O"]:
            return False

        # capraz kontrol
        if [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]]==["X","X","X"] or [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]]==["O","O","O"]:
            return False
        if [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]]==["X","X","X"] or [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]]==["O","O","O"]:
            return False

        return True




oyun=Oyun()

while oyun.durum:
    oyun.oyna()
