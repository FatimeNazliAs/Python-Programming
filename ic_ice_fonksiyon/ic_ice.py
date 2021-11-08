"""#encapsulation

def outer(num1):
    print('outer',num1)
    def inner_increment(num1):
        print('inner')
        return num1+1
    num2=inner_increment(num1)
    print(num1,num2)

outer(10)"""

def factorial(num):
    if not isinstance(num,int):
        raise TypeError("number must be an integer")

    if not num>=0:
        raise ValueError("Number must be zero or positive")
    def inner_fac(num):
        if num<=1:
            return 1


        return num*inner_fac(num-1)

    return inner_fac(num)
try:
    print(factorial(5))

except Exception as ex:
    print(ex)
