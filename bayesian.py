"""
NAME - AJINKYA PADWAD
HOMEWORK3 - BAYESIAN PREDICTIVE DISTRIBUTION
"""
import numpy	# library for numerical calculations
import math		# mathematics library
import csv		# library to open CSV file

"""
def openfile():
	csv = numpy.genfromtxt ('eggs.csv', delimiter=",")
	data = csv[0:5]
	print data
	return data
"""
# function to find the performance
def performance(meanvalue, average):	
	print ''
	print 'Performance - '
	meanvalue = round(meanvalue, 4)		# rounding up the mean predicted value
	relative = numpy.fabs(((meanvalue - average) / average)) * 100	# relative error
	
	#relative = numpy.fabs(round(relative, 3))		# rounding up to 3 digits
	print 'Relative Error : ', relative 

	value = []				# list to store final values
	value.append(meanvalue)	# append mean predicted value
	value.append(relative)	# append relative error value
	print 'Forecast :' , value

# function to find absolute mean
def avg(targetdata, meanvalue):
	sum = 0		# sum of all input values

	for a in targetdata:
		sum += a
	average = sum / len(targetdata)
	print 'Actual average :', average
	print 'Calculated prediction average : ', meanvalue
	performance(meanvalue, average)

# function to find the prediction value
def prediction(data):
	exponents =[]	# powers of x in phix(n)
	targetdata = []	# target array for data
	target=[]		# target array for transition
	N = 10			# max number of elements
	M = 6			# max order of polynomial
	alpha = 0.005	# standard value of alpha, based on noise
	beta = 11.1		# standard value of beta, based on noise


	for i in range(len(data) - N, len(data)):	# take latest 10 data values
		targetdata.append(data[i])				# store int target array for data

	for i in range(1, 11):						# exponents 1,2,3...10
		exponents.append(i)						# store in array
	
	x = exponents[len(exponents) - 1]			# initiate x as last element of exponents 
	# reshaping to proper size 
	target.append(targetdata)	
	targetdata = target
	
	target = numpy.zeros((N,1),float)			# resizing and initializing

	# initializing three terms of the expression
	phiX      = numpy.zeros((M,1),float)
	sigmaphiX = numpy.zeros((M,1),float)
	sigmaT    = numpy.zeros((M,1),float)

	for i in range(M):
		phiX[i][0]=math.pow(x,i)				# loading x^1, x^2, ... x^n into phi(x)

	for i in range(N):							# mapping list to matrix
	  	target[i][0]=targetdata[0][i]
	
	for j in range(N): # finding summation values
		for i in range(M):
			sigmaphiX[i][0]=sigmaphiX[i][0]+math.pow(exponents[j],i)		# term for mean
			sigmaT[i][0]=sigmaT[i][0]+target[j][0]*math.pow(exponents[j],i)	# term for variance

	# get S matrix
	S = numpy.linalg.inv(alpha*numpy.identity(M)+beta*numpy.dot(sigmaphiX,phiX.T))

	# calculate variance
	variance = (1/beta) + numpy.dot((phiX.T),numpy.dot(S,phiX))

	# calculate mean
	mean=beta*numpy.dot(phiX.T,numpy.dot(S,sigmaT))
	
	# print mean
	meanvalue = mean[0][0]	

	target = targetdata[0] # take the first row
	targetdata = target
	avg(targetdata, meanvalue)	# call average function

#data = openfile()

# data set from Yahoo Finance for EA company stocks-
data = [85.45,84.46,86.34,83.31,86.20,86.44,87.43,87,85.43,84.34]

	# data set from Yahoo Finance for S & P company stocks-
#data = [2010.23,2011.34,2011.22,2010.56,2012.44,2010.12,2011.99,2011.10,2010.6,2012.67]

	# data set from Yahoo Finance for Dow 30 company stocks-
#data = [2755.45,2757.23,2766.34,2758.4,2758.9,2755.45,2757.23,2760.34,2756.3,2757.9]

	# data set from Yahoo Finance for NASDAQ company stocks-
#data = [5835.3,5836,5834.56,5835.56,5836.56,5837,5836,5834.93,5835.88,5837.56]


# data set from Yahoo Finance for EA company stocks-

print 'Stock prices : \n', data
prediction(data) # main command to run the prediction function
