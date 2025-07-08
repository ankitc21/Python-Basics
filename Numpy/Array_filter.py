import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

y=[True,True,False,False]
newarr=arr[y]
print(newarr)


#Creation of filter array:
arr = np.array([41, 42, 43, 44])
filter_arr=[]
for i in arr:
    if i>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(newarr)

#Creating Filter Directly From Array-->
arr = np.array([41, 42, 43, 44])
filter_arr=arr>42
newarr=arr[filter_arr]
print(newarr)