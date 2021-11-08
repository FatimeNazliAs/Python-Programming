
"""a=int(input('a: '))
b=int(input('b: '))
result=(a>b)
print(f'a: {a} b: {b} den büyüktür: {result}')

vize1 =float(input('1.vize: '))
vize2 =float(input('2.vize: '))
final =float(input('final: '))
ort = ((vize1+vize2)/2*0.6)+(final*0.4)
print(f'not ortalamanız: {ort} ve dersten geçme durumunuz: {ort>=50}')

sayi =int(input('sayi: '))
tekcift = (sayi%2 ==0)
print(f'girilen sayı çift olma durumu: {tekcift}') """

email = 'email@sadikturan.com'
password ='abc123'
girilenEmail=input('email: ')
girilenPassword = input('parola: ')

isEmail =(email==girilenEmail)
isPassword =(password ==girilenPassword)

print(f'Email dogru mu: {isEmail} ve Parola dogru mu: {isPassword}')
