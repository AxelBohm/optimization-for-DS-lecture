import numpy as np

def policeman_and_burglar_matrix(n, th=0.8):
    w = np.abs(np.random.randn(n))
    th = 0.8
    C = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            C[i,j] = np.abs(i-j)
    A = w * (1 - np.exp(-th * C))
    return A