# Importing Low-Level LAPACK functions

from numpy.lib.utils import info
import scipy.linalg.lapack as la
import numpy as np
import time

# Creating Matrix system

a = np.array([[2, 1, 0, 0, 0], [1, 2, 1, 0, 0], [0, 1, 2, 1, 0], [0, 0, 1, 2, 1], [0, 0, 0, 1, 2]])
b = np.array([[4], [4], [0], [0], [2]])

#Solving System as DENSE

result1 = la.dgesv(a, b)

print(result1)
print(time.process_time())

#Solving System as DENSE and SYMMETRIC

n = 5       #The number of linear equations, i.e., the order of the matrix A.  N >= 0.

ap = np.array([2, 1, 2, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 2])

result2 = la.dppsv(n, ap, b )

print(result2)
print(time.process_time())

#Solving System as BAND
'''
rr = 5;     #Rank.
kl = 1;     #Number of lower diagonals.
ku = 1;     #Number of upper diagonals.
nrhs = 1;   #Number of RHS.
'''
ab = np.array([1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 1, 1, 2, 1, 1])
'''
result3 = la.dgbsv(kl, ku, ab, b)

print(result3)

print(time.process_time)
'''
#Solving System as BAND and SYMMETRIC

result4 = la.dpbsv(ab, b)

print(result4)
print(time.process_time())
''''
#Solving System as TRIDIAGONAL

dl = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
d = np.array([2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
du = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])

result5 = la.dgtsv(dl, d, du, b)

print(result5)
print(time.process_time())

#Solving System as TRIDIAGONAL and SYMMETRIC

d = np.array([2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
e = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

result6 = la.dptsv(d, e, b)

print(result6)
print(time.process_time())

'''