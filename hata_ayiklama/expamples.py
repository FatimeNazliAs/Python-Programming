"""liste=["1","2","5a","10b","abc","10","50"]

for x in liste:
    try:
        result=int(x)
        print(result)

    except ValueError:
        continue


while True:
    x = input("sayi girin: ")
    if x == "q":
        break

    try:
        result = float(x)
        print(result)

    except ValueError:
        print("gecersiz sayı")


def parola_kontrolu():
    turkce='şçüöıi'
    parola=input("parola: ")

    for i in parola:
        if i in turkce:
            raise TypeError("parola turkce karakter iceremez.")
        else:
            pass
    print("gecerli parola")


try:
    parola_kontrolu()

except TypeError as err:
    print(err)"""

def faktoriyel(x):
    x=int(x)

    if x<0:
        raise ValueError("Negatif deger")

    result=1
    for i in range(1,x+1):
        result*=i

    return result

for x in [5,6,7,-3,'10a']:

    try:
        y=faktoriyel(x)


    except Exception as err:
        print(err)
        #continue


    print(y)





