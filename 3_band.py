# Importing Low-Level LAPACK functions

from numpy.lib.utils import info
import scipy.linalg.lapack as la
import numpy as np
import time
import random

# Creating Matrix system

for n in range(10000, 10001):
    kl = 1
    ku = 1
    rows_ab = int(2*kl+ku+1)
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
            if (max(1, l-ku) <= k) and (k <= min(n, l+kl)):
                ind = int(kl+ku+1+k-l)
                ind = ind-1                
                AB[ind][j] = A[i][j]

#Solving System as BAND

result3 = la.dgbsv(kl, ku, AB, b)

print(result3)

print(time.process_time())