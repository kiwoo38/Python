import random

originNumber=[]

for i in range(3):
    originNumber.append(random.randrange(1,9))

print(originNumber)

for i in range(5):
    originNumber.append(random.randrange(10,100,5))

print(originNumber)