from memory_profiler import profile
from linear_queue import LinearQueue
from find_n import find_n
import time

def populate_queues(n):
    """Crea colas con tamaños n, 2n, 3n, 4n, 5n y las llena de elementos."""
    queues = {
        'n': LinearQueue(n),
        '2n': LinearQueue(2 * n),
        '3n': LinearQueue(3 * n),
        '4n': LinearQueue(4 * n),
        '5n': LinearQueue(5 * n)
    }

    # Poblar cada cola con elementos
    for key, queue in queues.items():
        for i in range(queue.max):
            queue.enqueue(f'Element-{i}')  # Usamos un string como elemento

    return queues

# Agregar decoradores para perfilado

def run_search_n(queue):
    """Ejecutar búsqueda en la cola de tamaño n"""
    print(f"Searching in queue of size {queue.max}")
    queue.search("Element-NOT-FOUND")  # Buscar un elemento que no existe
    time.sleep(1)  # Pausa de 1 segundo

def run_dequeue_n(queue):
    """Ejecutar operación dequeue en la cola de tamaño n"""
    print(f"Dequeue in queue of size {queue.max}")
    queue.dequeue()  # Eliminar un elemento
    time.sleep(1)  # Pausa de 1 segundo

def run_all_tests(queues):
    """Ejecutar todas las pruebas de búsqueda y eliminación."""
    
    # Realizar las 5 pruebas de search
    for key, queue in queues.items():
        run_search_n(queue)  # Buscar un elemento que no existe en la cola
    
    # Realizar las 5 pruebas de dequeue
    for key, queue in queues.items():
        run_dequeue_n(queue)  # Eliminar un elemento de la cola

if __name__ == "__main__":
    # Encontrar el valor de n
    n = find_n()
    print(f"Value of n: {n}")
    queues = populate_queues(n)

    print("Starting all tests...")
    run_all_tests(queues)