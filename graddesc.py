import numpy as np
import matplotlib.pyplot as plt
import math

# goal: find best fit polynomial for values of sin

def integ(fn, lb, ub, N):
    """
    Integral function from the textbook Computer Science with Applications by 
    Professors Borja Sotomayor and Anne Rogers. Approximates an integral with a 
    midpoint Riemann Sum.

    Inputs:
        fn (function): the function whose integral will be taken
        lb (int): the lower bound of the integral
        ub (int): the upper bound of the integral
        N (int): the number of partitions

    Returns: the integral of the function fn from the lower bound
        to the upper bound, approximated with N partitions
    """

    delta = (ub - lb)/N 
    sum = 0
    for i in range(N):
        sum += delta * fn(lb + delta * (i + 0.5))
    return sum

def least_squares(fn1, fn2):
    """
    Returns a function evaluating the least-squares difference bewteen two
    functions

    Inputs:
        fn1 (function): the first function
        fn2 (function): the second function
    
    Returns: a function evaluating the least-squares difference between fn1 and
        fn2.
    """
    def leastsqx(x):
        """
        Evaluates the least-squares function at a specific input x

        Input:
            x (int): an input value
        
        Returns: the least-squares function evaluated at input x
        """
        return (fn1(x) - fn2(x))**2
    return leastsqx

#maybe abstract this one even more
def polynomial_approx(a0, a1, a2, a3, a4, a5):
    """
    Inspired by Khan Academy function--a polynomial that approximates a 
    function using coefficients a0 through a5.

    Inputs:
        a0...a5 (int): the coefficients of the polynomial
    
    Returns: a function to calculate the polynomial for a given input
    """
    def polapproxx(x):
        """
        Evaluates the polynomial for an input x

        Input:
            x (int): the input value for the polynomial
        
        Returns: the polynomial evaluated for input x
        """
        return (a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5)

    return polapproxx


def least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5):
    """
    The least-squares integral from Khan Academy generalized for any upper or
    lower bound. Integrates the least-squares difference function
    of two functions from a lower bound to an upper bound. Specified for
    polynomial approximation of sin(x) and sin(x)--but easily generalizable.

    Inputs:
        lb (int): the lower bound of the integral
        ub (int): the upper bound of the integral
        N (int): the number of partitions for the integral
        a0...a5 (int): the coefficients of the polynomial

    Returns: the least-squares integral from lb to ub of sin(x) and its
        approximation with N partitions.
    """
    result = integ(least_squares(polynomial_approx(a0, a1, a2, a3, a4, a5),
        math.sin), lb, ub, N)
    return result

def grad_desc(lb, ub, N, a0, a1, a2, a3, a4, a5):
    """
    A rudimentary form of gradient descent--checks what the effect
    would be of increasing or decreasing each coefficient on the value of the
    least-squares integral function. If a decrement decreases the value,
    the variable is decremented; if an increment increases it, the variable is
    incremented. Runs until the increment falls below a certain value,
    then returns a list of the coefficients.

    To change the increment, keeps track of whether or not the least-squares
    integral value has changed from one iteration to the next. If not, it is an
    indication that the (de/in)ncrement has too high of an absolute value, so it
    is resized by a factor of ten.

    Inputs:
        lb (int): the lower bound of the least-squares intgeral
        ub (int): the upper bound of the least-squares integral
        N (int): the number of partitions of the least-squares integral
        a0...a5 (int): the coefficients of the polynomial
    """

    # number of times the value of the least_squares_integral has been the same
    repeated = 0

    # decrement/increment by which to change each coefficient
    inc = 10

    while (inc > 0.000001):
        # a0
        lsi_init = least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)
        if (least_squares_integral(lb, ub, N, a0-inc, a1, a2, a3, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a0 -= inc
        elif (least_squares_integral(lb, ub, N, a0+inc, a1, a2, a3, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a0 += inc
        print(f"a0: {a0}\n")
        #   this is repeated below for each coefficient ai
    # returns a list of the coefficients

        #a1
        if (least_squares_integral(lb, ub, N, a0, a1-inc, a2, a3, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a1 -= inc
        elif (least_squares_integral(lb, ub, N, a0, a1+inc, a2, a3, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a1 += inc
        print(f"a1: {a1}\n")

        #a2
        if (least_squares_integral(lb, ub, N, a0, a1, a2-inc, a3, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a2 -= inc
        elif (least_squares_integral(lb, ub, N, a0, a1, a2+inc, a3, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a2 += inc
        print(f"a2: {a2}\n")

        #a3
        if (least_squares_integral(lb, ub, N, a0, a1, a2, a3-inc, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a3 -= inc
        elif (least_squares_integral(lb, ub, N, a0, a1, a2, a3+inc, a4, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a3 += inc
        print(f"a3: {a3}\n")

        #a4
        if (least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4-inc, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a4 -= inc
        elif (least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4+inc, a5)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a4 += inc
        print(f"a4: {a4}\n")

        #a5
        if (least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5-inc)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a5 -= inc
        elif (least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5+inc)
            < least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)):
            a5 += inc
        print(f"a5: {a5}\n")

        lsi_new = least_squares_integral(lb, ub, N, a0, a1, a2, a3, a4, a5)
        if lsi_new == lsi_init:
            repeated += 1
        if repeated > 1:
            repeated = 0
            inc /= 10

    return [a0, a1, a2, a3, a4, a5]

valsa = grad_desc(-3,3,30,0,0,0,0,0,0)
print(valsa)
x = np.linspace(-3, 3, 100)

# valsa: list of values returned by grad_desc_actual

# generate array of values of the approximation on [-3, 3]
y1 = np.array([polynomial_approx(valsa[0], valsa[1], valsa[2], valsa[3], 
    valsa[4], valsa[5])(xi) for xi in x])

#generate the actual values of sin(x) on [-3, 3]
y2 = np.array([math.sin(xi) for xi in x])

plt.plot(x, y1, 'r--', x, y2, 'b--')
plt.savefig('plot.png')
print('Red line indicates the approximation; blue the sine function\n')