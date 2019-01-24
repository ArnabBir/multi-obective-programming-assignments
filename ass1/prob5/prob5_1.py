import matplotlib.pyplot as plt
import numpy as np

def f1(x1, x2):
	return x1*x1 + x2*x2

def f2(x1, x2):
	return (x1-5)*(x1-5) + (x2-5)*(x2-5)

def main():
	
	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	x1 = np.linspace(0, 5, 100)
	x2 = np.linspace(0, 5, 100)
	x1x2 = []
	for i in x1:
		for j in x2:
			x1x2.append([i,j])
	series_f1 = [f1(x[0], x[1]) for x in x1x2]
	series_f2 = [f2(x[0], x[1]) for x in x1x2]
	plt.scatter(series_f1, series_f2)
	#plt.fill_between(series_f1, series_f2, color = 'grey', alpha = 0.5)
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel(r'$f1(x)$')
	plt.ylabel(r'$f2(x)$')
	plt.show()

main()