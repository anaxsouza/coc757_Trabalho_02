# Importing Low-Level LAPACK functions

from numpy.lib.utils import info
import scipy.linalg.lapack as la
import numpy as np
import time
import random

# Creating Matrix system

for n in range(2000, 2001):
    A = np.zeros((n, n))
    b = np.zeros(n)    
    D = np.zeros(n)
    E = np.zeros(n-1)
    cont1 = 0
    cont2 = 0

    for i in range(n):
        b[i] = random.random()
        for j in range(n):
            if i == j:
                A[i][j] = random.random()
            if (i - j) == -1:
                A[i][j] = random.random()
                A[j][i] = A[i][j]

    for i in range(n):
        for j in range(n):
            if i == j:
                D[cont1] = A[i][j]
                cont1 = cont1 +1
            if (i-j) == 1:
                E[cont2] = A[i][j]
                cont2 = cont2 +1
                
#Solving System as TRIDIAGONAL and SYMMETRIC

result6 = la.dptsv(D, E, b)

print(result6)
print(time.process_time())
