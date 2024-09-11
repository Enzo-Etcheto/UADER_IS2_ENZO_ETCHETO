import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt

#*------------------------------------------------------------------------------------------------
#* Almacena dataset historico
#*------------------------------------------------------------------------------------------------
data = {
    'LOC': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Esfuerzo': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

#*------------------------------------------------------------------------------------------------
#* Inicializacion del programa
#*------------------------------------------------------------------------------------------------
version="7.0"
linear=False
exponential=False
os.system('clear')

#*------------------------------------------------------------------------------------------------
#* Procesa argumentos
#*------------------------------------------------------------------------------------------------
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-v", "--version", required=False, help="version", action="store_true")
ap.add_argument("-x", "--exponential", required=False, help="Exponential model", action="store_true")
ap.add_argument("-l", "--linear", required=False, help="Linear model", action="store_true")
args = vars(ap.parse_args())

if args['version'] == True:
    print("Program %s version %s" % (sys.argv[0], version))
    sys.exit(0)

if args['linear'] == True:
    print("Program %s version %s" % (sys.argv[0], version))
    print("Linear correlation model selected")
    linear = True

if args['exponential'] == True:
    print("Program %s version %s" % (sys.argv[0], version))
    print("Exponential correlation model selected")
    exponential = True

if linear == False and exponential == False:
    print("Program %s version %s" % (sys.argv[0], version))
    print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")

#*------------------------------------------------------------------------------------------------
#* Definir dataset y procesar correlacion entre LOC (complejidad) y Esfuerzo (PM)
#*------------------------------------------------------------------------------------------------
df = pd.DataFrame(data)

#*------------------------------------------------------------------------------------------------
#* Procesa modelo lineal, usa numpy polyfit()
#*------------------------------------------------------------------------------------------------
if linear == True:
    a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
    R = np.corrcoef(df['LOC'], df['Esfuerzo'])
    R2 = R[1][0] ** 2

    print("Modelo lineal E=%.6f + %.6f*LOC" % (b, a))
    print("El R-squared=%.4f (lineal)" % (R2))

    # Graficar el modelo lineal
    lbl = ("Modelo lineal (R-Sq=%.2f)" % (R2))
    plt.plot(df['LOC'], a * df['LOC'] + b, label=lbl, color='red')

#*------------------------------------------------------------------------------------------------
#* Procesa modelo exponencial utiliza OLS fit()
#*------------------------------------------------------------------------------------------------
if exponential == True:
    df['logEsfuerzo'] = np.log(df['Esfuerzo'])
    df['logLOC'] = np.log(df['LOC'])

    X = df['logLOC']
    Y = df['logEsfuerzo']
    X = sm.add_constant(X)  # Añadir constante

    mx = sm.OLS(Y, X).fit()
    print(mx.summary())

    k = np.exp(mx.params['const'])
    b = mx.params['logLOC']

    print("Modelo exponencial E=%.6f * (LOC^%.6f)" % (k, b))
    print("El R-squared=%.2f (exponencial)" % (mx.rsquared))

    # Graficar el modelo exponencial
    lbl = ("Modelo exponencial (R-Sq=%.2f)" % (mx.rsquared))
    plt.plot(df['LOC'], k * (df['LOC'] ** b), label=lbl, color='green')

#*------------------------------------------------------------------------------------------------
#* Predicciones para LOC=9100 y LOC=200
#*------------------------------------------------------------------------------------------------
LOC_9100 = 9100
LOC_200 = 200

if linear:
    esfuerzo_9100_linear = a * LOC_9100 + b
    esfuerzo_200_linear = a * LOC_200 + b
    print(f"Prediccion lineal para LOC=9100: {esfuerzo_9100_linear:.2f} PM")
    print(f"Prediccion lineal para LOC=200: {esfuerzo_200_linear:.2f} PM")

if exponential:
    esfuerzo_9100_exp = k * (LOC_9100 ** b)
    esfuerzo_200_exp = k * (LOC_200 ** b)
    print(f"Prediccion exponencial para LOC=9100: {esfuerzo_9100_exp:.2f} PM")
    print(f"Prediccion exponencial para LOC=200: {esfuerzo_200_exp:.2f} PM")

#*------------------------------------------------------------------------------------------------
#* Hace plot del dataset historico
#*------------------------------------------------------------------------------------------------
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos historicos')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()

# Precaucion para LOC=200
if LOC_200 < df['LOC'].min():
    print("Advertencia: LOC=200 esta fuera del rango historico, lo que puede disminuir la confiabilidad del modelo.")
