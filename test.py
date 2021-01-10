from bracketingMethod.bracketingMethod import *

# f = lambda x: x**2 - x - 1
f = "x**2 - x - 1"
bracketing_method('bisection', f, 0, 5, 10)

# Bisection method
# f = lambda x: 8 - 4.5 * (x - sin(x))
# print(bisection(f, 2, 3, 5))

# False-position
# g = lambda x: x**3 - x - 1
# print(false_position(g, 0, 2, 5))

# Secant method
# p = lambda x: x**3 - x**2 - 1
# print(secant(p, 1, 2, 20))