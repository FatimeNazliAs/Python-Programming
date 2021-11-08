"""x=0
while x<20:
    if x%2==0:
        print(f'sayi cift: {x}')
    else:
        print(f'sayi tek: {x}')
    x += 1


i=0
sayilar =[1,3,5,7,9,12,19,21]

while i<len(sayilar):
    print(sayilar[i])
    i+=1
"""


"""x=int(input('kucuk sayi: '))
y=int(input('buyuk sayi: '))

while x<y:
    print(x)
    x += 1


a=100
while a>50:
    print(a)
    a-=1


x=0
sayilar= []
while x<5:
    sayi=int(input('sayi giriniz: '))
    sayilar.append(sayi)
    x+=1
sayilar.sort()
print(sayilar)

urunler = []
urun_sayisi=int(input('ürün sayısını giriniz '))

i=0

while i<urun_sayisi:
    name=input('urun adi: ')
    price=int(input('urun fiyatı: '))
    urunler.append({
        'ad': name,
        'fiyat': price
    })
    i+=1


for urun in urunler:
    print(f"ürün adı: {urun['ad']} ürün fiyatı: {urun['fiyat']}")



name = 'Nazlı As'
for letter in name:
    if letter == 'z':
        continue
    print(letter)

x=0
while x<5:
    x += 1
    if x==2:
        continue
    print(x)
"""




