import os
from datetime import datetime
#print(dir(os))


#os.mkdir("newdirectory")#dosya olusturma
# os.chdir('C:\\')#change directory
# result=os.getcwd()#konum gosterme
# print(result)

#os.makedirs("newdirectory/yeniklasor")
# os.rename("newdirectory","yeni")

# result=os.listdir()
# print(result)
#
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

result=os.stat("datetimeee.py")
#result=result.st_size/1024#dosyanın byte cinsinden boyutu
# result=datetime.fromtimestamp(result.st_ctime)#olusturulma tarihi
# print(result)

# os.system("notepad.exe")

result=os.path.abspath("os_module.py")
result=os.path.dirname(os.path.abspath("os_module.py"))#tam yol üzerinden dizin ismi
result=os.path.exists("os_module.py")
result=os.path.isfile("C:/Users/betul-pc/PycharmProjects/Btk_Python/ileri_seviye_moduller/os_module.py")
print(result)
