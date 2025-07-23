import matplotlib.pyplot as plt
import seaborn as sns

#Histogram plotting-->

sns.displot([0, 1, 2, 3, 4, 5,100,200])
plt.show()

#Plotting without histogram-->

sns.displot([0,1,2,3,4,5],kind='kde')
plt.show()