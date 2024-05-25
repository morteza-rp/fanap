import numpy as np

def win_fail(array):
    if np.max(array) > 70:
        return "Win"
    else:
        return "Fail"

