from math import *


# Parameters: function, lower bound, upper bound, number of iterations
def secant(func, a, b, N):
    # Output will be a dictionary in form
    # {lower bound, upper bound, function at lower bound, function at upper bound, new bound, function at new bound}
    result = {}

    f = lambda x: eval(func)
    if f(a) * f(b) >= 0:
        print("Secant method fails.")
        return None
    a_i = a
    b_i = b
    for n in range(N + 1):
        m_n = a_i - f(a_i) * (b_i - a_i) / (f(b_i) - f(a_i))
        f_m_n = f(m_n)
        result[n] = [a_i, b_i, f(a_i), f(b_i), m_n, f_m_n]
        if f(a_i) * f_m_n < 0:
            a_i = a_i
            b_i = m_n
        elif f(b_i) * f_m_n < 0:
            a_i = m_n
            b_i = b_i
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return result
