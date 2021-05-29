# Importing Low-Level LAPACK functions

from numpy.lib.utils import info
import scipy.linalg.lapack as la
import numpy as np
import time
import random

# Creating Matrix system

for n in range(10000, 10001):
    A = np.zeros((n,n))
    b = np.zeros(n)

    for i in range(n):        
        b[i] = random.random()
        for j in range(n):
            if i == j:
                A[i][j] = random.random()
            if (i - j) == -1:
                A[i][j] = random.random()
                A[j][i] = A[i][j]

#Solving System as DENSE

result1 = la.dgesv(A, b)

print(result1)
print(time.process_time())