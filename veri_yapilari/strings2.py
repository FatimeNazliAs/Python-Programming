"""name = 'nazli'
surname = 'as'
age=20
greeting = 'my name is '+name+' '+surname+ ' and \nI am '+str(age)+' years old.'
print(greeting)
print(greeting[-1])
print(len(greeting))
print(greeting[3:])
print(greeting[2:40:2])"""

#format
ad='melis'
soyad='yilmaz'
#print('my name is {} {}'.format(ad,soyad))
#print('my name is {1} {0}'.format(ad,soyad))
print('my name is {s} {n}'.format(n=ad,s=soyad))
print('my name is {} {} and I am {} years old'.format(ad,soyad,20))

print(f'my name is {ad} {soyad} and I am {20} years old.')


