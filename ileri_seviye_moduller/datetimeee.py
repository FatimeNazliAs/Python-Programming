from datetime import datetime
from datetime import timedelta
simdi=datetime.now()

# print(simdi.day)
# print(simdi.hour)

# result=datetime.ctime(simdi)
# result=datetime.strftime(simdi,'%Y')
# result=datetime.strftime(simdi,'%X')
# result=datetime.strftime(simdi,'%d')
# result=datetime.strftime(simdi,'%A')
# result=datetime.strftime(simdi,'%Y %B %A')
# print(result)

t='15 April 2019 hour 10:12:30'
dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt.year)

birth=datetime(1983,5,9,12,30,10)
result=datetime.timestamp(birth)#saniye cinsinden verir
result=datetime.fromtimestamp(result)#saniyeyi datetime ceviriri
result=datetime.fromtimestamp(0)#1970 bilgisayarlar icin milat

print(result)

result=simdi-birth #timedelta
result=result.days
print(result)

print(simdi)
result=simdi+timedelta(days=10,minutes=10)
print(result)

