# profile_operations.py
import cProfile
import pstats
from populate_queues import populate_queues  # Importar la función populate_queues
from find_n import find_n

def profile_operations():
    n = find_n()  # Llamar a la función find_n para obtener el valor de n
    queues = populate_queues(n)  # Llamar a populate_queues para llenar las colas

    # Definir un elemento que no existe en las colas
    non_existent_element = 'Element-999999'

    # Perfilando la búsqueda de un elemento que no existe
    print("Profiling search for a non-existent element:")
    profiler = cProfile.Profile()
    profiler.enable()
    
    for key, queue in queues.items():
        queue.search(non_existent_element)
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()

    # Perfilando la operación de dequeue
    print("\nProfiling dequeue operation:")
    profiler = cProfile.Profile()
    profiler.enable()
    
    for key, queue in queues.items():
        queue.dequeue()  # Realiza una operación de dequeue
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()

if __name__ == "__main__":
    profile_operations()