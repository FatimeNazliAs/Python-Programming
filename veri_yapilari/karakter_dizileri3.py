"""website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


length =len(website)
result = website[7:10]
print(result)
result = website[-3:]
print(result)

result = course[:15]
print(result)
result = course[::-1] #ters yazdırma

print(result)"""

name,surname,age,job = 'bora','yılmaz',32,'mühendis'
result = 'benim adım {} {}, yaşım {} ve mesleğim {}.'.format(name,surname,age,job)
print(result)
result = f"benim adım {name} {surname}, yaşım {age} ve mesleğim {job}."
print(result)
