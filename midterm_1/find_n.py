from linear_queue import LinearQueue
import time

def find_n():
    n = 1000  # Empezamos con un número arbitrario
    while True:
        queue = LinearQueue(n)
        start_time = time.time()
        for i in range(n):
            queue.enqueue(str(i))
        elapsed = time.time() - start_time
        if elapsed >= 1:  # Cambiar a 1 segundo
            return n
        n *= 2  # Duplicar n si no alcanza el segundo

# Imprimir el tamaño n encontrado
print(find_n())