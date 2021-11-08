def changeName(n):
    n='ada'

name ='yiğit'
changeName(name)
print(name)


def change(n):
    n[0]='istanbul'


sehirler = ['ankara','izmir']
change(sehirler)
print(sehirler)

def add(*p):
    return sum((p))

print(add(10,20,30))
print(add(10,20))
print(add(10,20,30,40))


def displayUser(**args):
    for key,value in args.items():
        print('{} is {}'.format(key,value))



displayUser(name='Cınar',age=2,city='istanbul')
displayUser(name='Ada',age=12,city='kocaeli',phone='123')
displayUser(name='Yigit',age=14,city='ankara',email='yigit@gmail.com')


def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


myfunc(10,20,30,40,key1='value1',key2='value2')

#liste icin *,dictinoary icin **

#UYGULAMALAR

def printfunc(word,number):
    n = 0
    while n<number:
        print(word)
        n+=1


printfunc('nazli',5)


def listeyeCevir(*p):
    liste=[]
    for i in p:
        liste.append(i)

    return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)



def prime(x,y):

    isPrime=True
    for n in range(x,y+1):
        if(n==0):
            print("0 is not prime")
            continue

        if (n == 1):
            print("1 is not prime")
            continue

        for i in range(2,n):
            if (n%i==0):
                isPrime=False
                break


        if isPrime:
            print(f"{n} is prime")

        else:
            print(f"{n} is not prime")

        isPrime = True



prime(1,19)


def tamBolen(num):
    bolenler=[]
    for i in range(2,num):
        if (num % i== 0):
            bolenler.append(i)

    return bolenler


result =tamBolen(30)
print(result)
