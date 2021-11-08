"""numbers=[1,2,3,4,5]

for num in numbers:
    print(num)

name = 'Sadik Turan'
for n in name:
    print(n)


tuple = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b)


d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

d={'k1':1,'k2':2,'k3':3}
for key,value in d.items():

    print(value)

#examples
x=0
sayilar =[1,3,5,7,9,12,19,21]
for s in sayilar:
    x+=s
    if s%2!=0:
        print(s*s)


print('toplam',x)

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for s in sehirler:
    if len(s)<=5:
        print(s)"""


urunler=[
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'},
]

toplam =0
for urun in urunler:
    fiyat =int(urun['price'])
    toplam += fiyat

print('toplam ürün fiyatı',toplam)

for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])