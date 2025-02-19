import cProfile
import random

def slow_function():
    total = 0
    for _ in range(10**6):
        total += random.randint(1, 100)
    return total

cProfile.run('slow_function()')
