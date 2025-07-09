import numpy as np
arr=np.array([1,2,3,4,5,6])
x=np.where(arr==5)
print(x)
'''
# for finding out odd and even values-->'''
y=np.where(arr%2==0)        #index values even
z=np.where(arr%2!=0)        #Index values odd
print(y)
print(z)