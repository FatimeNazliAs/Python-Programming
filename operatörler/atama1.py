"""x,y,z=5,10,20
x,y=y,x

x+=5
y+=6
z//=5 #tam bolme
z**=3
print(x,y,z)

values =1,2,3
print(type(values))
x,y,z=values
print(x,y,z)"""


x,y,z=2,5,10
numbers =1,5,7,10,6

x,*y,z=numbers

print(x,y,z)
result=z**3
print(result)