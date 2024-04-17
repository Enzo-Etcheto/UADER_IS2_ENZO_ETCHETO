class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class CalculadoraImpuestos(metaclass=SingletonMeta):
    def calcular_impuestos(self, monto_base):
        tasa_iva = 0.21
        tasa_iibb = 0.05
        tasa_impuesto_municipal = 0.012

        iva = monto_base * tasa_iva
        iibb = monto_base * tasa_iibb
        impuesto_municipal = monto_base * tasa_impuesto_municipal

        total_impuestos = iva + iibb + impuesto_municipal
        return total_impuestos

calculadora_impuestos = CalculadoraImpuestos()

monto_base = 1000
total_impuestos = calculadora_impuestos.calcular_impuestos(monto_base)
print("Total de impuestos a pagar:", total_impuestos)