"""def tambolenler(x):
    liste=[]
    i=1
    for i in range(i,x):
        if x%i==0:
            liste.append(i)

    return liste



x=int(input("Bir sayı giriniz:  "))
print(tambolenler(x))"""


def ekok(a,b):
    ek=a*b
    for sayi in range(ek,max(a,b)-1,-1):
        if sayi%a==0 and sayi%b==0:
            ek=sayi
    return ek





sayi1=int(input("birinci sayı giriniz: "))
sayi2=int(input("ikinci sayı giriniz: "))

print(ekok(sayi1,sayi2))




