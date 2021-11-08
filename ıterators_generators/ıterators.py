
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# liste=[1,2,3,4,5]

# iterator=iter(liste)
# while True:
#     try:
#         element=next(iterator)
#         print(element)
#     except StopIteration:
#         break

class new_range:
    def __init__(self,start,end):
        self.yazilacak=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.yazilacak>=self.end:
            raise StopIteration
        deger=self.yazilacak
        self.yazilacak+=1
        return deger


sayilar=new_range(10,20)
for i in sayilar:
    print(i)


