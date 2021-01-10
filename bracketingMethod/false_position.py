from math import *


# Parameters: function, lower bound, upper bound, number of iterations, desired tolerance
def false_position(func, a, b, N, err=False):
    # Output will be a dictionary in form
    # {lower bound, upper bound, function at lower bound, function at upper bound, new bound, function at new bound, error}
    result = {}

    f = lambda x: eval(func)
    
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None

    a_i = a
    b_i = b

    # if desired tolerance is not defined, err == False
    if not err:
        for n in range(N + 1):
            x_c = ((a_i * f(b_i)) - b_i * f(a_i)) / (f(b_i) - f(a_i))
            f_x_c = f(x_c)
            result[n] = [a_i, b_i, f(a_i), f(b_i), x_c, f_x_c]
            if f(a_i) * f_x_c < 0:
                a_i = a_i
                b_i = x_c
            if f(a_i) * f_x_c > 0:
                a_i = x_c
                b_i = b_i
            elif f_x_c == 0:
                # print("Found exact solution.")
                result["Exact solution"] = x_c
                return result
            else:
                # print("Bisection method fails.")
                return None
        return result

    # if desired tolerance is defined, err != False
    if err:
        n = 0
        while err:
            x_c = ((a_i * f(b_i)) - b_i * f(a_i)) / (f(b_i) - f(a_i))
            f_x_c = f(x_c)
            result[n] = [a_i, b_i, x_c, f(a_i), f(b_i), f_x_c]
            if f(a_i) * f_x_c < 0:
                a_i = a_i
                b_i = x_c
            if f(a_i) * f_x_c > 0:
                a_i = x_c
                b_i = b_i
            elif f_x_c == 0:
                # print("Found exact solution.")
                result["Exact solution"] = x_c
                return result
            else:
                # print("Bisection method fails.")
                return None
            # check if the approximation of the root is acceptable
            m_n = abs((b_i - a_i) / 2)
            result[n].append(m_n)
            if m_n < err:
                return result
            n += 1