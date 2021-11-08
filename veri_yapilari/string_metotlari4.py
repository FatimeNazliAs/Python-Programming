message = 'Hello There. My name is Nazlı As.'

"""message= message.upper()
message= message.lower()
message= message.title()
message= message.capitalize() #sadece bas harf

message= message.strip() #bastaki boslugu siler
message= message.split() #kelimeleri ayırır
message= message.split('.')
message =' * '.join(message)

index = message.find('Nazlı')
print(index)
print(message)
isFound = message.startswith('H')
print(isFound)
isFound = message.endswith('.')
print(isFound)"""


message = message.replace('Nazlı','Betul')
message = message.replace(' ','--')
message = message.center(50,'*')
print(message)


