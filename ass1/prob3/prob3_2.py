import matplotlib.pyplot as plt
import numpy as np

def f1(x1, x2):
	return 0.4*x1 + 0.3*x2

def f2(x1, x2):
	return x1

def main():
	
	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	x1 = np.array([0, 4, 0, 0])
	x2 = np.array([0, 0, 4, 0])
	series_f1 = f1(x1, x2)
	series_f2 = f2(x1, x2)
	plt.plot(series_f1, series_f2)
	plt.fill_between(series_f1, series_f2, color = 'grey', alpha = 0.5)
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel(r'$f1(x)$')
	plt.ylabel(r'$f2(x)$')
	plt.show()

main()