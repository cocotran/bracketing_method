from .bisection import *
from .false_postition import *
from .secant import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

# Bisection method
# f = lambda x: 8 - 4.5 * (x - sin(x))
# print(bisection(f, 2, 3, 5))

# False-position
# g = lambda x: x**3 - x - 1
# print(false_position(g, 0, 2, 5))

# Secant method
# p = lambda x: x**3 - x**2 - 1
# print(secant(p, 1, 2, 20))

def bracketing_method(name, f, a, b, N, err=False):
	if name == 'bisection':
		# Get data
		data = list(bisection(f, a, b, N, err).values())
		root = [i[4] for i in data]
		# Ploting
		x = np.linspace(a,b,100)
		n = [0 for i in range(len(root))]
		# Plotting function
		fig, axis = plt.subplots(nrows=2, ncols=1)
		axis[0].plot(x, eval(f))
		axis[0].plot(root, n, "|")
		# Plotting error
		if err != False:
			error = [i[6] for i in data]
			axis[1].plot(n, error)

		# Plot
		axis[0].grid()
		axis[1].grid()
		plt.show()

	# if name == 'false_position':
	# 	return false_position(f, a, b, N, err)
	# if name == 'secant':
	# 	return secant(f, a, b, N)