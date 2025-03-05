import matplotlib.pyplot as plt
import numpy as np

# Datos extraídos del perfil de memoria para stacks
tamanos = np.array([ 130100, 260200, 390300, 520400, 650500])

# Tiempos aproximados en MB basados en el perfil de memoria
tiempos_push = np.array([260203, 520403, 780603, 1040803, 1301003])

tiempos_pop = np.array([0.0, 0.0, 0.0, 0.0, 0.0])  # No se muestra decremento significativo

# Convertir valores negativos a positivos para visualizar en la gráfica
tiempos_push = np.abs(tiempos_push)
tiempos_pop = np.abs(tiempos_pop)

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(tamanos, tiempos_push, marker='o', linestyle='-', label='Push (Inserción en Stack)')
plt.plot(tamanos, tiempos_pop, marker='s', linestyle='--', label='Pop (Eliminación de Stack)')

# Etiquetas y título
plt.xlabel('Tamaño del Stack (n)')
plt.ylabel('Tiempo de ejecución (MB)')
plt.title('Comparación de tiempos de inserción y eliminación en un Stack')
plt.legend()
plt.grid()

# Guardar la gráfica
plt.savefig('push_pop_stack_plot.png')
plt.show()

