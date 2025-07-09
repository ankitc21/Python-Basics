import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[0:7])
#Negative Slicing-->
print(arr[-3:-1])
#Step-->
print(arr[1:5:2])
print(arr[::2])
#Slicing 2-D Arrays-->
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d[1,::2])

arr_01= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr_01[0:2, 2])