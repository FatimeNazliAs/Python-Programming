"""name='Çınar'
def changeName(new_name):
    name=new_name
    print(name)

changeName('Ada')
print(name)


x=50
def test():
    global x
    print('x '+str(x))
    x=100
    print('changed x to '+str(x))

test()
print(x)"""

#bankamatik uygulaması

SadikHesap={
    'ad':'Sadık Turan',
    'hesapNo':'132456',
    'bakiye':3000,
    'ekHesap':2000
}

AliHesap={
    'ad':'Ali Turan',
    'hesapNo':'178956',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print(f"paranızı alabilirsiniz ve {hesap['bakiye']-miktar} paranız kaldı")
    else:
        toplam =hesap['bakiye'] +hesap['ekHesap']

        if toplam>=miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı(e/h): ')

            if ekHesapKullanimi=='e':
                ekKullanilicakMiktar =miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekKullanilicakMiktar
                print(f'paranızı alabilirsiniz ve {toplam-miktar} paranız kaldı')

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl paranız vardır")
        else:
            print(f"üzgünüz bakiye yetersiz ve {miktar-(hesap['bakiye']+hesap['ekHesap'])} kadar paranız eksiktir.")


paraCek(SadikHesap,4000)
paraCek(SadikHesap,2000)