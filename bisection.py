from math import *


def bisection(f, a, b, N):
    result = {}

    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(N + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        result[n] = [a_n, b_n, m_n, f(a_n), f(b_n), f_m_n]
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            result["Exact solution"] = m_n
            return result
        else:
            print("Bisection method fails.")
            return None
    return result


# f = lambda x: (2 * x - 1) * (x - 3)
# print(bisection(f, 0, 1, 10))

# f = lambda x: x**2 - x - 1
# print(bisection(f, 1, 2, 5))

f = lambda x: 8 - 4.5 * (x - sin(x))
print(bisection(f, 2, 3, 5))