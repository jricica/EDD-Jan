from memory_profiler import profile
import numpy as np

@profile 
def test_list():
    lst =  [i for i in range (10**6)]
    return lst

@profile 
def test_numpy():
    arr = np.arange(10**6)
    return arr

test_list()
test_numpy()