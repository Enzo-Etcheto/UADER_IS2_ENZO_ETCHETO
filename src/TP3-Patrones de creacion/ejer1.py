"""Ejecicio 1: Provea una clase que dado un número entero cualquiera retorne el factorial del
mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
instancia de clase.

Uso de Singleton
"""
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class factorial(metaclass=SingletonMeta):
    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

# Uso del Singleton factorial
factorial_calculator = factorial()

# Calculando factorial
print("El resultado es:",factorial_calculator.calculate_factorial(5)) 
print("El resultado es:",factorial_calculator.calculate_factorial(3))