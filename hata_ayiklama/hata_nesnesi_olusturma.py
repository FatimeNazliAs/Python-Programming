import re
def check_password(psw):
    if len(psw)<8:

        raise Exception("parola en az 8 karakter olmalıdır")
    elif not re.search("[a-z]",psw):
        raise Exception("parola kucuk harf icermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola buyuk harf icermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam icermelidir")
    elif not re.search("[_@$]", psw):
        raise Exception("parola alpha numeric karakter icermelidir")

password="12345678 "

try:
    check_password(password)

except Exception as ex:
    print(ex)
else:
    print("gecerli parola")




