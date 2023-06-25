import numpy as np
import matplotlib.pyplot as plt
import math
import random
import statistics

# goal: find best fit polynomial for values of sin

def integ(fn, lb, ub, N):
	"""
	From Computer Science with Applications by borya and rogers
	"""

	delta = (ub - lb)/N
	sum = 0
	for i in range(N):
    	sum += delta * fn(lb + delta * (i + 0.5))
	return sum

def least_squares(fn1, fn2):
	"""
	From Khanacademy: takes two functions, finds least squares
	difference between them at a given input
	"""
	def leastsqx(inp):
    	"""
    	Returns w input
    	"""
    	return (fn1(inp) - fn2(inp))**2
	return leastsqx

	return (a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5)
def random_poly():
	"""
	generate random polynomial
	"""
	a0, a1, a2, a3, a4, a5 = random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10)
	def randompolx(x):
    	return (a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5)
	return randompolx

rando = random_poly()
#create specific instance of random poly

#maybe abstract this one even more
def polynomial_approx(a0, a1, a2, a3, a4, a5):
	"""
	From Khanacademy: approximates polynomial with constants and
	x val
	"""
	def polapproxx(x):
    	return (a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5)
	return polapproxx


def grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5):
	"""
	From Khanacademy: least squares integral
	"""
	result = integ(least_squares(polynomial_approx(a0, a1, a2, a3, a4, a5),
    	pol_secure), lb, ub, N)
	return result

def grad_desc_actual(lb, ub, N, a0, a1, a2, a3, a4, a5, inc, tol):
	"""
	Own attempt
	"""
	i = 100
	while (grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5) > tol):
    	# a0
    	if (grad_desc_original(lb, ub, N, a0-inc, a1, a2, a3, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a0 -= inc
    	elif (grad_desc_original(lb, ub, N, a0+inc, a1, a2, a3, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a0 += inc

    	print(f"a0: {a0}\n")

    	#a1
    	if (grad_desc_original(lb, ub, N, a0, a1-inc, a2, a3, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a1 -= inc
    	elif (grad_desc_original(lb, ub, N, a0, a1+inc, a2, a3, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a1 += inc
    	print(f"a1: {a1}\n")

    	#a2
    	if (grad_desc_original(lb, ub, N, a0, a1, a2-inc, a3, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a2 -= inc
    	elif (grad_desc_original(lb, ub, N, a0, a1, a2+inc, a3, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a2 += inc
    	print(f"a2: {a2}\n")

    	#a3
    	if (grad_desc_original(lb, ub, N, a0, a1, a2, a3-inc, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a3 -= inc
    	elif (grad_desc_original(lb, ub, N, a0, a1, a2, a3+inc, a4, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a3 += inc
    	print(f"a3: {a3}\n")

    	#a4
    	if (grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4-inc, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a4 -= inc
    	elif (grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4+inc, a5)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a4 += inc
    	print(f"a4: {a4}\n")

    	#a5
    	if (grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5-inc)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a5 -= inc
    	elif (grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5+inc)
        	< grad_desc_original(lb, ub, N, a0, a1, a2, a3, a4, a5)):
        	a5 += inc
    	print(f"a5: {a5}\n")
    	i += 1
	return [a0, a1, a2, a3, a4, a5]

def pol_secure(x):

	return (2 + 3*x + 6*x**2 + 2*x**3 + 8*x**4 + 5*x**5)

def grad_descend_recurs(lb, ub, N, a0, a1, a2, a3, a4, a5):
	"""
	recurses grad desc
	"""
	tol = statistics.mean([abs(pol_secure(-3)),abs(pol_secure(-2)),abs(pol_secure(0)),abs(pol_secure(2)),abs(pol_secure(3))])/100
	inc = tol/1000
	toltol = 0.01*tol
	while (tol > toltol):
    	avals = grad_desc_actual(lb, ub, N, a0, a1, a2, a3, a4, a5, inc, tol)
    	a0, a1, a2, a3, a4, a5 = avals
    	inc *= 0.9
    	tol *= 0.9
    	print(inc, tol)
	return avals



valsa = grad_descend_recurs(-3,3,10000,1,2,3,4,5,6)
print(valsa)
x = np.linspace(-3, 3, 100)

#pass x as input to polynomial approx for the a values found
y1 = np.array([polynomial_approx(valsa[0], valsa[1], valsa[2], valsa[3],
	valsa[4], valsa[5])(xi) for xi in x])

y2 = np.array([pol_secure(xi) for xi in x])

plt.plot(x, y1, 'r--', x, y2, 'b--')
plt.savefig('plot.png')

