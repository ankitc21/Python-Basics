import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[2])
print(arr[3]+arr[5])

#Access 2-D Arrays-->
arr_2d= np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr_2d[0][2]+arr_2d[1][4])
print(arr_2d[1,-1])

#Access 3-D Arrays-->
arr_3d= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d[1][0][1])
print(arr_3d[1,0,1])