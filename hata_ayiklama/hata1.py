
"""try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)

except (ZeroDivisionError,ValueError) as e:
    print("yanlıs bilgi girdiniz")
    print(e)"""


while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)

    except Exception as ex:
        print("yanlıs bilgi girdiniz",ex)


    else:
        break

    finally:
        print("try except sonlandı.")



