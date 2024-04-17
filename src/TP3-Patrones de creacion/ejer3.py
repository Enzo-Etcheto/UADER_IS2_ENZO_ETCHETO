from abc import ABC, abstractmethod

class FabricaComidaRapida(ABC):
    @abstractmethod
    def crear_comida(self) -> 'ComidaRapida':
        pass

class ComidaRapida(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def entregar(self):
        pass

class Hamburguesa(ComidaRapida):
    def preparar(self):
        print("Preparando hamburguesa...")

    def entregar(self):
        print("Hamburguesa lista para ser entregada.")

class FabricaHamburguesas(FabricaComidaRapida):
    def crear_comida(self) -> ComidaRapida:
        return Hamburguesa()

def cliente(fabrica: FabricaComidaRapida) -> None:
    comida = fabrica.crear_comida()
    comida.preparar()
    comida.entregar()

if __name__ == "__main__":
    fabrica_hamburguesas = FabricaHamburguesas()
    cliente(fabrica_hamburguesas)