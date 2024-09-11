import numpy as np
import matplotlib.pyplot as plt

# Funcion para calcular el esfuerzo E basado en el tamaño del proyecto S
def calcular_esfuerzo(S):
    return 8 * S**0.95

# Funcion para calcular el tiempo de desarrollo td basado en el esfuerzo E
def calcular_tiempo(esfuerzo):
    return 2.4 * esfuerzo**0.33

# Rango de valores de S y calculo de E
tamanos = np.linspace(0, 10000, 400)
esfuerzos = calcular_esfuerzo(tamanos)

# Grafico de E en funcion de S
plt.figure(figsize=(10, 5))
plt.plot(tamanos, esfuerzos, label='Esfuerzo (E) vs Tamaño del proyecto (S)')
plt.title('Esfuerzo requerido por tamaño del proyecto')
plt.xlabel('Tamaño del Proyecto (S)')
plt.ylabel('Esfuerzo (E)')
plt.grid(True)
plt.legend()
plt.show()

# Rango de valores de E para calcular td
esfuerzo_rango = np.linspace(1, 500, 400)
tiempos = calcular_tiempo(esfuerzo_rango)

# Grafico de td en funcion de E
plt.figure(figsize=(10, 5))
plt.plot(esfuerzo_rango, tiempos, label='Tiempo de Desarrollo (td) vs Esfuerzo (E)')
plt.title('Tiempo de desarrollo por esfuerzo')
plt.xlabel('Esfuerzo (E)')
plt.ylabel('Tiempo de Desarrollo (td)')
plt.grid(True)
plt.legend()
plt.show()