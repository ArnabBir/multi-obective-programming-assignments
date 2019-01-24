import matplotlib.pyplot as plt
import numpy as np

def g1(x):
	return 4-x

def g2(x):
	return 500-2*x

def main():
	
	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	x1 = np.linspace(0, 4, 1000)
	series_g1 = g1(x1)
	series_g2 = g2(x1)
	plt.plot(x1, series_g1, label=r'$g1(x)\leq4$')
	plt.plot(x1, series_g2, label=r'$g2(x)\leq500$')
	plt.fill_between(x1, x1*0, np.minimum(series_g1, series_g2), color = 'grey', alpha = 0.5)
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel(r'$x1$')
	plt.ylabel(r'$x2$')
	plt.show()

main()