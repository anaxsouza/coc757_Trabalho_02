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

lu, piv, x, info = la.dgesv(a, b)

print(result1)
print(time.process_time())

#Solving System as DENSE and SYMMETRIC


#Solving System as BAND
rr = 5;     #Rank.
kl = 1;     #Number of lower diagonals.
ku = 1;     #Number of upper diagonals.
nrhs = 1;   #Number of RHS.
ab = np.array([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1])

result2 = la.dgbsv(kl, ku, ab, b)

print(result2)

time.process_time

#Solving System as BAND and SYMMETRIC

#Solving System as TRIDIAGONAL

#Solving System as TRIDIAGONAL and SYMMETRIC


