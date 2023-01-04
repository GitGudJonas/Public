############ Aestheticc enter #########
import numpy as np
import matplotlib.pyplot as plt

# import scipy as scp
# import csv
#######################################
'''
Our goal for this project is to create a program that:
Takes n inputs in the form of (x,y) coordinates
Yields a best fit polynomials of deg \leq n
Constraints:
n>2

Heavily Linear Algebra based

Changelog
ver 0.1
basic framework with manual code modification for everything
ver 0.2
displaying graph with results
TODO:
prevent errors and sanity check reqs
allow tuple input via GUI

'''

# Tuples entry
tuples=[]
tuples.append((1,2))
tuples.append((2,3))
tuples.append((4,4))
tuples.append((5,5))
# manual entry for now, will create GUI later

# Determine degree of fit polynomial
deg=2

# Tuples to matrix conversion
tup=np.array(tuples)
f=tup.take(0,1)
B=tup.take(1,1)
A=np.ones((len(tuples),1))
for i in range(0,deg):
    
    A=np.insert(A,i+1,np.power(f,i+1),axis=1)
    
# print(A)
B=np.transpose(B)
# print(B)

# Matrix with tuples to construct inconsistent system

# In case system is consistent we can fit a line 

# Behind the scenes math stuff

lhs=np.matmul(np.transpose(A),A)
rhs=np.matmul(np.transpose(A),B)
sol=np.matmul(np.linalg.inv(lhs),rhs)

# sol prints coefficients from deg 0 to max deg.
print(sol)

def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of degree {o-1}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    
    return y


# sol prints coefficients from deg 0 to max deg.

x = np.arange(min(f)-1, max(f)+1, 0.1)
# PolyCoefficients(x,sol)
# print(y)
colors = np.random.rand(len(f))
plt.plot(x, PolyCoefficients(x, sol))
#plt.show()
# # colors = np.random.rand(len(tuples))
plt.scatter(f,B,c=colors)
plt.show()

