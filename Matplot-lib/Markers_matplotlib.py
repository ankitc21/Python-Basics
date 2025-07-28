import matplotlib.pyplot as plt
import numpy as np

y=np.array([3, 8, 1, 10])
plt.plot(y,marker='o')
plt.show()

'''Marker	Description -->

'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline'''


'''Line Reference
Line Syntax	Description -->

'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line'''


'''Color Reference -->

Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White	
'''


'''Marker Size
You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:'''
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

'''Marker Color
You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:'''
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()


'''You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:'''
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()