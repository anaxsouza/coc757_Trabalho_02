# Importing Low-Level LAPACK functions

from numpy.lib.utils import info
import scipy.linalg.lapack as la
import numpy as np
import time
import random

# Creating Matrix system

for n in range(10000, 10001):
    kd = 1
    rows_ab = int(kd+1)
    A = np.zeros((n, n))
    b = np.zeros(n)
    AB = np.zeros((rows_ab, n))

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
            k = i+1
            l = j+1
            #o = max(1, l-ku)
            #p = min(n, l+kl)
            if (max(1, l-kd) <= k) and (k <= l):
                ind = int(kd+1+k-l)
                ind = ind-1                
                AB[ind][j] = A[i][j]

#Solving System as BAND and SYMMETRIC

result4 = la.dpbsv(AB, b)

print(result4)
print(time.process_time())