import numpy as np
from random_number import generate_random_number

def array_generator(n):
    arr = np.array([])
    for i in range(n):
        arr = np.append(arr, generate_random_number())
    return arr