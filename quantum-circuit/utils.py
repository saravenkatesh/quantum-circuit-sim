import numpy as np

def ground(n):
    return np.array([1] + (2**n - 1)*[0])