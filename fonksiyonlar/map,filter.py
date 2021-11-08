def karesini_al(x):
    return x**2

sayilar=[*range(1,6)] #broadcast ile range'i listeye cevirdik
x=list(map(karesini_al,sayilar))
print(x)

def cift_sayilari_filtrele(x):
    return x if x%2==0 else None

print([*filter(cift_sayilari_filtrele,sayilar)])

print(list(map(lambda x:x**2,sayilar)))