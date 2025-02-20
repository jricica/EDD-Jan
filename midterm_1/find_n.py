# find_n.py
from linear_queue import LinearQueue
import time

def find_n():
    n = 1000  # Empezamos con un número arbitrario
    max_attempts = 10  # Límite de intentos
    attempts = 0

    while attempts < max_attempts:
        queue = LinearQueue(n)
        start_time = time.time()
        for i in range(n):
            queue.enqueue(str(i))
        elapsed = time.time() - start_time
        if elapsed >= 1:  # Cambiar a 1 segundo
            return n
        n *= 2  # Duplicar n si no alcanza el segundo
        attempts += 1  # Incrementar el contador de intentos

    return n  # Retornar el último valor de n si no se alcanzó el tiempo