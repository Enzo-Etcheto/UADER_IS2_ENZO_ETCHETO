from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def produce(self) -> str:
        pass

class ConcreteImplementation5(Implementation):
    def produce(self) -> str:
        return "Produciendo lamina de 5 metros de acero"

class ConcreteImplementation10(Implementation):
    def produce(self) -> str:
        return "Produciendo lamina de 10 metros de acero"

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def produce(self) -> str:
        return self.implementation.produce()

class LaminaAcero:
    def __init__(self, espesor: float, ancho: float, tren_laminador: Abstraction) -> None:
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir_lamina(self) -> None:
        print(f"Produciendo lamina de acero de {self.espesor} pulgadas de espesor y {self.ancho} metros de ancho")
        print(self.tren_laminador.produce())

if __name__ == "__main__":

    implementation5 = ConcreteImplementation5()
    implementation10 = ConcreteImplementation10()

    abstraction5 = Abstraction(implementation5)
    abstraction10 = Abstraction(implementation10)

    lamina1 = LaminaAcero(0.5, 1.5, abstraction5)
    lamina2 = LaminaAcero(0.5, 1.5, abstraction10)

    lamina1.producir_lamina()
    print("\n")
    lamina2.producir_lamina()