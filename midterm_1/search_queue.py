# search_queue.py
from populate_queues import populate_queues  # Importar la función populate_queues
from find_n import find_n

def search_in_queues(queues, test_key):
    results = {}
    for key, queue in queues.items():
        found = queue.search(test_key)
        results[key] = found
    return results

if __name__ == "__main__":
    n = find_n()  # Llamar a la función find_n para obtener el valor de n
    queues = populate_queues(n)  # Llamar a populate_queues para llenar las colas

    # Imprimir solo el tamaño de cada cola
    for key, queue in queues.items():
        print(f'{key} size: {queue.max}')

    # Probar el método search
    # Buscamos algunos elementos que sabemos que están en las colas
    test_keys = [f'Element-{i}' for i in range(5)]  # Buscamos los primeros 5 elementos

    for test_key in test_keys:
        search_results = search_in_queues(queues, test_key)

        # Imprimir resultados de búsqueda
        for key, found in search_results.items():
            print(f'Searching for {test_key} in {key}: {found}')