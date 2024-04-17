from abc import ABC, abstractmethod

class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def obtener_condicion_impositiva(self):
        pass

class FacturaIVAResponsable(Factura):
    def obtener_condicion_impositiva(self):
        return "Factura para cliente IVA Responsable"

class FacturaIVANoInscripto(Factura):
    def obtener_condicion_impositiva(self):
        return "Factura para cliente IVA No Inscripto"

class FacturaIVAExento(Factura):
    def obtener_condicion_impositiva(self):
        return "Factura para cliente IVA Exento"

class FacturaFactory:
    def crear_factura(self, importe, condicion_impositiva):
        if condicion_impositiva == "IVA Responsable":
            return FacturaIVAResponsable(importe)
        elif condicion_impositiva == "IVA No Inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion_impositiva == "IVA Exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Condicion impositiva no valida")

factura_factory = FacturaFactory()

factura1 = factura_factory.crear_factura(1000, "IVA Responsable")
print(factura1.obtener_condicion_impositiva())

factura2 = factura_factory.crear_factura(1500, "IVA No Inscripto")
print(factura2.obtener_condicion_impositiva())

factura3 = factura_factory.crear_factura(800, "IVA Exento")
print(factura3.obtener_condicion_impositiva())