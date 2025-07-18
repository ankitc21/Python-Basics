from numpy import random
arr=random.choice([3,6,9,12,15],p=[0.2,0.15,0.6,0.02,0.03],size=(10)) #size = number of distribution to be obtained
print(arr)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))#probability is with respect to each values so numbers==probability
print(x)