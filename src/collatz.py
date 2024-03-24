import matplotlib.pyplot as plt
import numpy as np

def collatz(n):

    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia

numeros = np.arange(1, 10001)
longitudes = []
for numero in numeros:
    secuencia = collatz(numero)
    longitud = len(secuencia)
    longitudes.append(longitud)

plt.plot(numeros, longitudes)
plt.xlabel("Número inicial")
plt.ylabel("Número de iteraciones")
plt.title("Conjetura de Collatz (2n+1)")
plt.show()

plt.savefig("src/collatz.png")