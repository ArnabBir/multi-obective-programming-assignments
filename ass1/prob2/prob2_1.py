import matplotlib.pyplot as plt
import numpy as np

def main():
	
	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	x1 = np.linspace(0, 3, 100)
	x2 = np.linspace(0, 3, 100)
	plt.plot(x1, x1*0 + 3, label=r'$y\leq3$')
	plt.plot(x1, x1*0, label=r'$y\geq0$')
	plt.fill_between(x1, x1*0, x1*0 + 3, color = 'grey', alpha = 0.5)
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlim((0,5))
	plt.ylim((0,5))
	plt.xlabel(r'$x1$')
	plt.ylabel(r'$x2$')
	plt.show()

main()