# Importing Low-Level LAPACK functions

from numpy.lib.utils import info
import scipy.linalg.lapack as la
import numpy as np
import time
import random

# Creating Matrix system
for n in range(10000, 10001):
    n_ap = int(n*(n+1)/2)
    A = np.zeros((n, n))
    b = np.zeros(n)
    AP = np.zeros((n_ap))

    for i in range(n):
        b[i]=random.random()
        for j in range(n):
            if i == j:
                A[i][j]=random.random()
            if (i - j) == -1:
                A[i][j]=random.random()
                A[j][i]=A[i][j]

    for i in range(n):
        for j in range(n):
            k = i+1
            l = j+1
            if (k <= l):
                ind = int(k+l*(l-1)/2)
                ind = ind-1
                AP[ind]=A[i][j]
    
    result2 = la.dppsv(n,AP, b)

    print(result2)
    print(n, time.process_time())
