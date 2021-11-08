"""import random
import os
print("Select a random element from a list:")
elements = [1, 2, 3, 4, 5]
print(random.choice(elements))
print(random.choice(elements))
print(random.choice(elements))
print("\nSelect a random element from a set:")
elements = set([1, 2, 3, 4, 5])
# convert to tuple because sets are invalid inputs
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print("\nSelect a random value from a dictionary:")
d = {"a": "naz", "b": "bet", "c": "aynur", "d": "islim", "e": "fehmi "}
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
print("\nSelect a random file from a directory.:")
print(random.choice(os.listdir("/")))"""

import random
"""import string
print("Generate a random alphabetical character:")
print(random.choice(string.ascii_letters))
print("\nGenerate a random alphabetical string:")
max_length = 50
str1 = ""
for i in range(random.randint(1, max_length)):
    str1 += random.choice(string.ascii_letters)
print(str1)
print("\nGenerate a random alphabetical string of a fixed length:")
str1 = ""
for i in range(10):
    str1 += random.choice(string.ascii_letters)
print(str1)"""

import random
"""import datetime
print("Generate a random integer between 0 and 6:")
print(random.randrange(5))
print("Generate random integer between 5 and 10, excluding 10:")
print(random.randrange(start=5, stop=10))
print("Generate random integer between 0 and 10, with a step of 3:")
print(random.randrange(start=0, stop=10, step=3))
print("\nRandom date between two dates:")
start_dt = datetime.date(2019, 2, 1)
end_dt = datetime.date(2019, 3, 1)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)
print(random_date)"""

x=random.uniform(0,1)
print(x)

list=[1,2,3,4]
random.shuffle(list)
print(list)

import types
def func():
    return 1

print(isinstance(func, types.FunctionType))
print(isinstance(func, types.LambdaType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(max, types.FunctionType))
print(isinstance(max, types.LambdaType))


import copy
nums_x = [1, [2, 3, 4]]
print("Original list: ", nums_x)
nums_y = copy.copy(nums_x)
print("\nCopy of the said list:")
print(nums_y)

nums = {"x":1, "y":2, 'zz':{"z":3}}
nums_copy = copy.deepcopy(nums)
print("\nOriginal dictionary :")
print(nums)



