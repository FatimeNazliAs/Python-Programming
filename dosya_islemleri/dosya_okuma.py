"""try:

    file=open("newfile2.txt","r")
    print(file)

except FileNotFoundError:
    print("dosya okuma hatası")

finally:
    file.close()"""

file = open("newfile.txt", "r",encoding="utf-8")
for i in file:
    print(i,end="")

file = open("newfile.txt", "r",encoding="utf-8")
content1= file.read()
print("icerik1")
print(content1)

file = open("newfile.txt", "r",encoding="utf-8")
content2= file.read()
print("icerik2")
print(content2)


file = open("newfile.txt", "r",encoding="utf-8")
content=file.read(5)
print(content)
content=file.read(4)
print(content)

print(file.readline(),end="")
print(file.readline(),end="")
liste=file.readlines()
print(liste)


with open("newfile.txt", "r",encoding="utf-8") as file:
    content=file.read()
    print(content)
    #file.seek(0)#kursoru başa gönderir
    print(file.tell())
    

