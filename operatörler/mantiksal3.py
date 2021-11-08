"""x =6
#result = 5<=x<10
result = x>5 and x<10
print(result)

result = (x<0) or (x % 2 == 0)
print(result)

x=int(input('x: '))
result = x>0 and x<100
print(result)

y = int(input('y: '))
result = y>0 and y%2==0
print(result)"""

vize1 = float(input('1.vize: '))
vize2 = float(input('2.vize: '))
final =float(input('final: '))
ort = ((vize1*0.3+vize2*0.3)+final*0.4)

#result = (ort>=50) and (final>=50)
#print(f'öğrencinin ortalaması: {ort} ve geçme durumu: {result}')

result = (ort>=50) or (final>=70)
print(f'öğrencinin ortalaması: {ort} ve geçme durumu: {result}')

"""a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result =(a>b) and (a>c)
print(f'a en büyük sayıdır: {result}')

result =(b>a) and (b>c)
print(f'b en büyük sayıdır: {result}')

result =(c>b) and (c>a)
print(f'c en büyük sayıdır: {result}')"""







