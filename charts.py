#to be completed: draw horizontal line, by either shifting axes or plotting a line

import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

def barChart():
	dataY = [-8.51,0.27,0.52] #Import data from csv
	dataX = ['Energy For Production','GDP','Household Consumption']
	n_groups = len(dataX)
	index = np.arange(n_groups)
	bar_width = 0.4
	width = 0.8
	fig,a = plt.subplots()
	plt.axhline(y = 0,xmin=0,xmax=4,linewidth = 2) #for horizontal line plotting
	# p1=a.bar(dataY	,dataX)
	p1 = plt.bar(index,dataY,bar_width,alpha=0.4,color='b',label = 'Nothing')
	plt.xticks(index + bar_width/2, dataX)
	print(a.get_position())

	def autolabel(rects):
		for rect in rects:
			height = rect.get_height()
			#-ve rect height??
			a.text(rect.get_x() + rect.get_width()/2., 1.05*height,
						'%f' % float(height),
						ha='center', va='bottom')
	autolabel(p1)
	plt.legend()
	plt.tight_layout()
	plt.show()



if __name__ == '__main__':
	barChart()
