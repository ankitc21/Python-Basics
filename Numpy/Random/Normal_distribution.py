''' Normal Distribution
The Normal Distribution is one of the most important distributions.

It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.'''

import numpy as np
from numpy import random
#Generate a random normal distribution of size 2x3:
v=random.normal(size=(2,3))
print(v)

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x=random.normal(loc=1,scale=2,size= (2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000),kind='kde')
plt.show()