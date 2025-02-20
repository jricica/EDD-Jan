import matplotlib.pyplot as plt
import numpy as np

# Datos extraídos del perfil de memoria
tamanos = np.array([1024000, 2048000, 3072000, 4096000, 5120000])

# Tiempos aproximados en MB basados en el perfil de memoria
tiempos_search = np.array([2048003, 4096003, 6144003, 8192003, 10240003
])
tiempos_delete = np.array([0.0, 0.0, 0.0, 0.0, 0.0])  # No se muestra decremento significativo

# Convertir valores negativos a positivos para visualizar en la gráfica
tiempos_search = np.abs(tiempos_search)
tiempos_delete = np.abs(tiempos_delete)

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(tamanos, tiempos_search, marker='o', linestyle='-', label='Search')
plt.plot(tamanos, tiempos_delete, marker='s', linestyle='--', label='Dequeue')

# Etiquetas y título
plt.xlabel('Tamaño de la cola (n)')
plt.ylabel('Tiempo de ejecución (MB)')
plt.title('Comparación de tiempos de búsqueda y eliminación en una cola')
plt.legend()
plt.grid()

# Guardar la gráfica
plt.savefig('search_dequeue_plot.png')
plt.show()
