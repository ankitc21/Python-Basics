import numpy as np
import matplotlib.pyplot as plt
y=np.array([3, 8, 1, 10])
plt.plot(y,ls='--')
#or plt.plot(y,ls='dotted')
#or plt.plot(y,linestyle='dotted')
plt.show()
plt.plot(y,ls='-.')
plt.show()

'''Line Styles
You can choose any of these styles -->
Style	Or
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	" or " '''
y=np.array([3, 8, 1, 10])
plt.plot(y, c='hotpink',linewidth = '20.5')
plt.show()

#Multiple Lines -->
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()