import numpy as np
from numpy import random

#The permutation() method returns a re-arranged array (and leaves the original array un-changed).

arr=np.array([2,4,6,7,8,9])
print(random.permutation(arr))


#The shuffle() method makes changes to the original array.

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)