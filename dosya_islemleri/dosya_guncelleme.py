#Eğer her seferinde kapatma işlemini yapmak istemiyorsak dosyaları farklı bir yol olan with yapısıyla açabiliriz.
"""with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(25)
    file.write("deneme")
with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())



with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nBetul As")
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())"""



with open("newfile.txt","r+",encoding="utf-8") as file:
    content=file.read()
    content="Efe Turan\n" + content
    #file.seek(0)
    file.write(content)
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())

#sayfa ortasında guncelleme

with open("newfile.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(1,"Ali Kokrmaz")
    print(liste)



