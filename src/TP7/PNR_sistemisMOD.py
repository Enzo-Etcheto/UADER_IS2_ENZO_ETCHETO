import pandas as pd
import numpy as np
import sys
import os
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.optimize import root_scalar
from scipy.integrate import quad
from scipy.optimize import root_scalar
import argparse

# Funciones de soporte

# Esfuerzo acumulado E(t)
def E_acum(K, a, t):
    return K * (1 - np.exp(-a * (t ** 2)))

# Esfuerzo instantaneo E(t)
def E(t, K, a):
    return 2 * K * a * t * np.exp(-a * t**2)

# Encuentra el tiempo donde el esfuerzo es cercano a cero
def find_near_zero(K, a, tolerance):
    def equation(t):
        return E(t, K, a) - tolerance
    result = root_scalar(equation, bracket=[0.1, 100], method='brentq')
    return result.root if result.converged else None

# Estima el esfuerzo maximo
def find_maximum(K, a):
    def negative_E(t):
        return -E(t, K, a)
    result = minimize_scalar(negative_E, bounds=(0, 100), method='bounded')
    t_max = result.x
    E_max = E(t_max, K, a)
    return t_max, E_max

# --- Modificacion para incluir el dataset historico de calibracion (simplificado)
data_hist = {
    'Story Points': [2, 3, 8, 5, 2, 13],
    'Hits': [1104, 1762, 6602, 1565, 2179, 8030]
}
df_hist = pd.DataFrame(data_hist)

# --- Procesa el modelo PNR (Punto a y b)
def pnr_model(K, a, t_data):
    E_fit = E(t_data, K, a)
    return E_fit

# --- Configuraciones iniciales del programa
Kp = 72  # Esfuerzo total de 72 PM para el proyecto
gamma = 0.9
version = "1.0"
os.system('clear')

# Datos historicos
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Tiempo en meses
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11, 6])  # Esfuerzo instantaneo en PM

# Calibracion del modelo (best-fit)
K = np.sum(E_data)  # Esfuerzo total del dataset
popt, _ = curve_fit(E, t_data, E_data, p0=[K, 0.1])
K_est, a_est = popt
print(f"Esfuerzo total K estimado: {K_est:.2f} PM, parametro a estimado: {a_est:.4f}")

# --- Grafico del dataset historico y modelo ajustado (Punto a)
t_fit = np.linspace(min(t_data), max(t_data), 100)
E_fit = pnr_model(K_est, a_est, t_fit)

plt.scatter(t_data, E_data, label='Datos Historicos', color='blue')
plt.plot(t_fit, E_fit, label='Modelo Ajustado', color='red')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo (PM)')
plt.title('Modelo Ajustado vs Datos Historicos')
plt.legend()
plt.show()

# --- Punto b: Distribucion de esfuerzo para proyecto de 72 PM
K_nuevo = 72
E_fit_nuevo = pnr_model(K_nuevo, a_est, t_fit)

plt.scatter(t_data, E_data, label='Datos Historicos', color='blue')
plt.plot(t_fit, E_fit_nuevo, label='Modelo para 72 PM', color='green')
plt.plot(t_fit, E_fit, label='Modelo Ajustado', color='red')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo (PM)')
plt.title('Distribucion de Esfuerzo para Proyecto de 72 PM')
plt.legend()
plt.show()

# --- Comentario sobre las diferencias (Punto b)
print("El modelo para el proyecto de 72 PM es mas compacto y reduce el esfuerzo en picos, pero distribuye de manera similar.")

# --- Punto c: Modificacion del parametro "a" al cuadruple
a_modificado = 4 * a_est
E_fit_modificado = pnr_model(K_nuevo, a_modificado, t_fit)

plt.plot(t_fit, E_fit_modificado, label='Modelo con a modificado (4x)', color='purple')
plt.plot(t_fit, E_fit_nuevo, label='Modelo para 72 PM', color='green')
plt.scatter(t_data, E_data, label='Datos Historicos', color='blue')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo (PM)')
plt.title('Efecto de Modificar el Parametro a (4x)')
plt.legend()
plt.show()

# --- Comentario sobre el efecto de "Zona Imposible" (Punto c)
print("Al aumentar 'a' al cuadruple, la curva se vuelve mas estrecha y el esfuerzo se concentra en menos tiempo. Esto podria llevar el proyecto a la 'Zona imposible' debido a la necesidad de recursos extremos en un corto periodo.")
