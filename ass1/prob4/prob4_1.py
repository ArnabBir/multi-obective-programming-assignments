import matplotlib.pyplot as plt
import numpy as np

def f1(x):
	return x*x

def f2(x):
	return (x-2)*(x-2)

def main():
	
	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	x = np.linspace(0, 2, 51)
	series_f1 = f1(x)
	series_f2 = f2(x)
	plt.plot(x, series_f1, label=r'$f1(x)=x^2$')
	plt.plot(x, series_f2, label=r'$f2(x)=(x-2)^2$', color='green')
	plt.scatter(x, np.maximum(series_f1, series_f2), label=r'$f(x)=max(f1(x), f2(x))$', color='red')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel(r'$x$')
	plt.ylabel(r'$f(x)$')
	plt.show()

main()