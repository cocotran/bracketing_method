from bisection import *
from false_postition import *
from secant import *

# Bisection method
f = lambda x: 8 - 4.5 * (x - sin(x))
print(bisection(f, 2, 3, 5))

# False-position
g = lambda x: x**3 - x - 1
print(false_position(g, 0, 2, 5))

# Secant method
p = lambda x: x**3 - x**2 - 1
print(secant(p, 1, 2, 20))