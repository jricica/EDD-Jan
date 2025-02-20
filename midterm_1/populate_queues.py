# populate_queues.py
from linear_queue import LinearQueue
from find_n import find_n

def populate_queues(n):
    # Crear las instancias de las colas
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

if __name__ == "__main__":
    n = find_n()  # Llamar a la función find_n para obtener el valor de n
    queues = populate_queues(n)

    # Imprimir solo el tamaño de cada cola
    for key, queue in queues.items():
        print(f'{key} size: {queue.max}')