from find_n import find_n
from linear_queue import LinearQueue
import time
from memory_profiler import memory_usage

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
        
        # Medir tiempo y memoria antes de llenar la cola
        start_time = time.perf_counter()
        
        # Cargar los elementos de a uno
        def _enqueue_operations():
            for i in range(size):
                queue.enqueue(str(i))  

        # Medir el uso de memoria y tiempo
        mem_usage = memory_usage((_enqueue_operations,), max_usage=True, interval=0.01)
        tiempo_total = time.perf_counter() - start_time
        
        # Imprimir el resultado con tiempo y memoria
        print(f"Queue {i + 1} (Size {size}): {size} time = {tiempo_total:.4f} ; memory = {mem_usage:.2f} MiB")

if __name__ == '__main__':
    main()
