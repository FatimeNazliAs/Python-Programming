def square(num): return num**2

numbers=[1,3,5,7,10,14]

"""result=list(map(square,numbers))
print(result)

for item in map(square,numbers):
    print(item)

square=lambda num: num**2
result=square(3)
print(result)"""

def check_even(num): return num%2==0

#result= list(filter(check_even,numbers))
result= list(filter(lambda num: num%2==0,numbers))
print(result)

