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
    DL = np.zeros(n-1)
    D = np.zeros(n)
    DU = np.zeros(n-1)
    cont1 = 0
    cont2 = 0
    cont3 = 0

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
            if (i-j) == -1:
                DU[cont2] = A[i][j]
                cont2 = cont2 +1
            if (i-j) == 1:
                DL[cont3] = A[i][j]
                cont3 = cont3 +1


#Solving System as TRIDIAGONAL

result5 = la.dgtsv(DL, D, DU, b)

print(result5)
print(time.process_time())