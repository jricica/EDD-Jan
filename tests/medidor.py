import time 
import random

N = 10**6
data = list(range(N))
random.shuffle(data)
lookup_set = set(data)

def linear_search (value):
    return value in data 

def set_search(value):
    return value in lookup_set

value_to_find = random.randint(0, N)

start = time.time()
linear_search(value_to_find)
end = time.time()
print(f"🔹 Búsqueda lineal: {end - start:.5f} s")

start = time.time()
set_search(value_to_find)
end = time.time()
print(f"🔹 Búsqueda con set: {end - start:.5f} s")