from numpy import random

#Generate Random Number-->

a=random.randint(100)
print(a)

x=random.rand(4)
print(x)
y=random.randint(1000,size=5)
print(y)

x=random.randint(10,size=(2,3))
print(x)

#Generate Random Number From Array
Ch=[1,2,4,5,6,7,8]
arr=random.choice(Ch)
arr_1=random.choice([12,5,6,7,10])
print(arr)
print(arr_1)
