import numpy as np
from matplotlib import pyplot as plt
import tkinter 

#input form={x value,y value,bias term}
x=np.array([
	[-2,4,-1],
	[4,1,-1],
	[1,6,-1],
	[2,4,-1],
	[6,2,-1], 
	])

#output
y=np.array([-1,-1,1,1,1])

for d, sample in enumerate(x):
	if d<2:#plot negative samples
		plt.scatter(sample[0],sample[1],s=120,marker='_',linewidths=2)
	else:#plot positive samples
		plt.scatter(sample[0],sample[1],s=120,marker='+',linewidths=2)

#plt.plot([-2,6],[6,0.5])
plt.show()