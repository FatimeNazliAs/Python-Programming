"""x=int(input('x: '))
y=int(input('y: '))

if x>y:
    print("x y'den büyüktür")
elif x==y:
    print("x y'ye esit")
else:
    print("y x'den büyüktür")

name = input('adiniz: ')
age = int(input('yasınız: '))
graduate = input('egitim durumunuz: ')

if age>= 18:
    if graduate == 'lise' or graduate == 'universite':
        print(f'{name} ehliyet alabilirsin. ')
    else:
        print(f'{name} egitim durumun uygun degil.')
else:
    print(f'{name} ehliyet alamazsın yasınız tutmuyor.')


sozlu1 =int(input('1.sözlü: '))
sozlu2 =int(input('2.sözlü: '))
yazili =int(input('Yazili: '))

ort =(sozlu1+sozlu2+yazili)/3

if ort>=85 and ort<100:
    print(f'ortalamanız {ort} ve notunuz 5')
elif ort>=70 and ort<84:
    print(f'ortalamanız {ort} ve notunuz 4')
elif ort>=55 and ort<69:
    print(f'ortalamanız {ort} ve notunuz 3')
elif ort>=45 and ort<54:
    print(f'ortalamanız {ort} ve notunuz 2')
elif ort>=25 and ort<44:
    print(f'ortalamanız {ort} ve notunuz 1')
else:
    print(f'ortalamanız {ort} ve notunuz 0')



sayi =int(input('sayi: '))
if (sayi >0):
    if (sayi %2 == 0):
        print('pozitif cift sayıdır')
    else:
        print('pozitif tek sayıdır')

else:
    print('negatif sayıdır')

a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

if (a>b) and(a>c):
    print('a en buyuk sayıdır.')
elif (b>a) and (b>c):
    print('b en buyuk sayıdır.')
elif (c>a) and (c>b):
    print('c en buyuk sayıdır.')"""

name = input('adınız: ')
kg =float(input('kilonuz: '))
hg =float(input('boyunuz: '))

index =kg/(hg**2)

if(index>=0) and(index<=18.4):
    print(f'{name} kilo indeksin: {index} ve zayıfsın')

if (index >18.4) and (index <= 24.9):
    print(f'{name} kilo indeksin: {index} ve normal')

if (index >24.9) and (index <= 29.9):
    print(f'{name} kilo indeksin: {index} ve kilolu')

if (index > 29.9) and (index <= 34.9):
    print(f'{name} kilo indeksin: {index} ve obez')

else:
    print('yanlıs bilgi girdiniz.')
