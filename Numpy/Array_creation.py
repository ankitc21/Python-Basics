import numpy as np
arr= np.array([1,2,3,4,5,6])
arr1=np.array((1,2,3,4,5,6))
print(arr)
print(type(arr))
print(arr.dtype)
print(arr1)
#1-D Arrays:
arr_1d= np.array([1,2,3,4,5,6])

#2-D Arrays:
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)

#3-D arrays
arr_3d=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[1,2,3]]])
print(arr_3d)

#Checking dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(np.ndim(a))
print(np.ndim(b))
print(np.ndim(c))
print(np.ndim(d))
# or
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#definig an array with dimensions-->
arr_n= np.array([1, 2, 3, 4], ndmin=5)
print(arr_n)
print(arr_n.ndim)