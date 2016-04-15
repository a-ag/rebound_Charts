#to be completed: draw horizontal line, by either shifting axes or plotting a line
#hover over functionality
#labels etc
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


def barChart_Longer(dataX,dataY):

	# dataY = [-8.51,0.27,0.52] #Import data from csv
	# dataX = ['Energy For Production','GDP','Household Consumption']
	n_groups = len(dataX)
	index = np.arange(n_groups)
	bar_width = 0.4
	width = 0.8
	fig,a = plt.subplots()
	plt.axhline(y = 0,xmin=0,xmax=4,linewidth = 2) #for horizontal line plotting
	# p1=a.bar(dataY	,dataX)
	p1 = plt.bar(index,dataY,bar_width,alpha=0.4,color='b',label = 'Nothing')
	plt.xticks(index + bar_width/2, dataX,rotation='vertical')
	print(a.get_position())

	def autolabel(rects):
		for y,rect in enumerate(rects):
			print y
			if dataY[y]<0:
				height = -rect.get_height()
				a.text(rect.get_x() + rect.get_width()/2., 1.05*height,
						'%f' % float(height),
						ha='center', va='bottom')
			else:
				height = rect.get_height()
			#-ve rect height??
				a.text(rect.get_x() + rect.get_width()/2., 1.05*height,
							'%f' % float(height),
							ha='center', va='bottom')
	autolabel(p1)
	plt.legend()
	plt.tight_layout()
	plt.show()

def scatterPlot(dataX,dataY):

	# http://stackoverflow.com/questions/7908636/possible-to-make-labels-appear-when-hovering-over-a-point-in-matplotlib
	# Check above link for implementing hover over

	x = max(dataX) - min(dataX)
	y = max(dataY) - min(dataY)

	area = x*y  # 0 to 15 point radiuses
	fig,a = plt.subplots()
	plt.scatter(dataX, dataY, s=area, alpha=0.5)

	def onpick(event):
		thisline = event.artist
		xdata = thisline.get_xdata()
		ydata = thisline.get_ydata()
		ind = event.ind
		print 'onpick points:', zip(xdata[ind], ydata[ind])

	fig.canvas.mpl_connect('pick_event', onpick)

	plt.show()



if __name__ == '__main__':


	fig6adataY = [2.34919,
				1.81197,
				1.27557,
				1.27037,
				1.17024,
				1.11725,
				1.05491,
				0.99924,
				0.97598,
				0.89067,
				-0.04517,
				-0.08595,
				-0.11493,
				-0.27525,
				-1.25152,
				-2.46113,
				-3.2995,
				-4.776,
				-4.8798,
				-10.86481]
	fig6adataX = [
		'Air transportation',
		'Transportation support activities',
		'Mining (except oil and gas)',
		'Paper manufacturing',
		'Chemical manufacturing',
		'Apparel manufacturing',
		'Petroleum products manufacturing',
		'Nonmetallic product manufacturing',
		'Support activities for mining',
		'Truck transportation',
		'Transportation equipment manufacturing',
		'Federal civilian',
		'State and local',
		'Federal military',
		'Pipeline transportation (486)',
		'Oil and gas extraction (211)',
		'Oil production',
		'Electricity generation',
		'Natural gas generation',
		'Coal production']

	fig6bdataY=[
		3.201,
		2.136,
		1.604,
		1.376,
		1.308,
		1.277,
		1.239,
		1.16,
		1.13,
		1.102
	]

	fig6bdataX = [
		'Air transportation',
		'Petroleum products manufacturing',
		'Pipeline transportation',
		'Paper manufacturing',
		'Nonmetallic mineral product manufacturing',
		'Truck transportation',
		 'Apparel manufacturing',
		'Oil and gas extraction',
		'Primary metal manufacturing',
		'Support activities for mining'
	]

	fig6cdataY = [
		14.35418,
		3.93757,
		2.66327,
		2.55996,
		1.6477,
		1.58356,
		1.48725,
		1.47899,
		1.04127,
		0.92851,
		-0.66683,
		-1.15267,
		-1.15436,
		-1.21486,
		-1.4651,
		-1.87945,
		-2.27494,
		-4.41278,
		-4.75228,
		-4.92838
	]

	fig6cdataX = [
		'Petroleum products manufacturing',
		'Air transportation',
		'Chemical manufacturing',
		'Paper manufacturing',
		'Transportation support activities',
		'Coal production',
		'Nonmetallic mineral manufacturing',
		'Support activities for mining',
		'Mining (except oil and gas)',
		'Truck transportation',
		'Accommodation',
		'Machinery manufacturing',
		'Oil production',
		'Miscellaneous manufacturing',
		'Transportation equipment manufacturing',
		'Electronic product manufacturing',
		'Water transportation',
		'Oil and gas extraction',
		'Electricity generation',
		'Natural gas generation'
	]


	fig7dataX = [
		-7.46913E-06,
		-0.004994712,
		-0.000494073,
		-0.231015233,
		-0.158207927,
		-0.009389587,
		-0.000201953,
		-0.011933041,
		-0.006603615,
		-0.000613812,
		-0.531323262,
		-0.015921288,
		-0.071744604,
		-0.028012174,
		-0.015166929,
		-0.020662387,
		-0.008877887,
		-0.006731969,
		-0.008542767,
		-0.009567067,
		-0.003033555,
		-0.002945004,
		-0.166363279,
		-0.037217302,
		-0.002587205,
		-0.153726356,
		-0.007968427,
		0.076660376,
		-0.367217779,
		-0.016475438,
		-0.098556017,
		-0.065719903,
		-0.400763747,
		-0.042586416,
		-0.000261709,
		-0.270730933,
		-0.008003146,
		-0.008210882,
		-0.085751821,
		-0.010578474,
		-0.004401356,
		-0.000521936,
		-0.07682249,
		-0.00054604,
		-0.021682728,
		-0.00704611,
		-0.003360878,
		-8.31261E-05,
		-0.008792104,
		-0.014691139,
		-0.00220635,
		-0.005402223,
		-0.028394023,
		-0.010283543,
		-0.334468545,
		-0.008355288,
		-0.075996405,
		-0.013821757,
		-0.027483608,
		-0.005670605,
		-0.00245666,
		-0.009137579,
		-0.008610108,
		-0.063385586,
		-0.040529554,
		-0.026383493,
		-0.240297218,
		-9.48063E-05
	]

	fig7dataY = [
		34.44393922,
		73.44499856,
		69.74346972,
		-18.01507398,
		13.79674149,
		8.899711799,
		68.50725878,
		25.03403471,
		26.93381819,
		4.643412601,
		3.934512946,
		10.69178514,
		24.66115052,
		26.7024081,
		13.84893226,
		-0.522810376,
		-12.09656416,
		-1.272926359,
		-0.369493089,
		-18.69017444,
		-0.60079548,
		-16.26551652,
		10.06227953,
		19.69550486,
		7.567258208,
		41.74189936,
		19.15500717,
		169.7890082,
		36.8246349,
		27.50485317,
		5.425287578,
		-4.278258535,
		53.01963514,
		13.52360523,
		-18.96274872,
		14.74200186,
		9.968785758,
		55.323305,
		25.19134479,
		14.60847037,
		-1.723287176,
		-7.579025848,
		3.675814681,
		-0.187408496,
		2.543597262,
		-3.080548982,
		-3.185446325,
		-30.12738946,
		4.051530349,
		14.84879095,
		4.123169624,
		-7.41155976,
		6.184255433,
		22.68942583,
		9.896088676,
		6.51418358,
		5.21800823,
		-5.146320036,
		-4.943345884,
		-3.332649988,
		-0.967740566,
		0.642994559,
		58.88073919,
		5.414435735,
		1.141842972,
		6.421868684,
		7.870655485,
		1.176761765]

	# barChart_Longer(fig6adataX,fig6adataY) #for 6a
	# barChart_Longer(fig6bdataX,fig6bdataY) #for 6b
	# barChart_Longer(fig6cdataX,fig6cdataY) #for 6c

	scatterPlot(fig7dataX,fig7dataY) #for 7
