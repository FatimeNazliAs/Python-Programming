import re #regular expression
# print(dir(re))

str="Python Kursu: Python Programlama Rehberiniz | 40 saat"

# result=re.findall("Python",str)

# result=re.split(" ",str)

# result=re.sub("\s","-",str)

# result=re.search("Python",str)
# result=result.start()
# result=result.string#nerde arama yapıyor


#REGULAR EXPRESSION

# result=re.findall("[abc]",str)
# result=re.findall("[sat]",str)
# result=re.findall("[a-e]",str)
# result=re.findall("[1-4]",str)
# result=re.findall("[^pyo]",str)

result=re.findall("...",str)#uclu ayırır
result=re.findall("^P",str)#P ile baslıyor mu
result=re.findall("t$",str)#P ile bitiyor mu
print(result)
