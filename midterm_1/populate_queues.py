from find_n import find_n
from linear_queue import LinearQueue
import time
import psutil
import os

def get_memory_usage():
    """Obtiene el uso de memoria actual del proceso en MiB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convertir bytes a MiB

def main():
    # Obtener el tamaño n
    n = find_n()
    print(f"Valor de n: {n}")  # Se imprime solo una vez al principio

    # Verificar que n sea positivo
    if n <= 0:
        raise ValueError("El tamaño n debe ser un número positivo.")

    # Asegurarse de que los tamaños sean exactamente n, 2n, 3n, 4n, 5n
    sizes = [n * i for i in range(1, 6)]  
    print(f"Tamaños de las colas: {sizes}")  # Imprime los tamaños de las colas solo una vez

    for i, size in enumerate(sizes):
        queue = LinearQueue(size)
        
        # Medir memoria antes de cargar la cola
        mem_before = get_memory_usage()

        # Medir tiempo antes de cargar la cola
        start_time = time.perf_counter()
        
        # Cargar los elementos de a uno
        for j in range(size):
            queue.enqueue(str(j))  

        # Medir tiempo después de cargar la cola
        tiempo_total = time.perf_counter() - start_time

        # Medir memoria después de cargar la cola
        mem_after = get_memory_usage()

        # Imprimir el resultado con tiempo y memoria
        print(f"Queue {i + 1} (Size {size}): {size} time = {tiempo_total:.4f} ; memory = {mem_after - mem_before:.2f} MiB")

if __name__ == '__main__':
    main()