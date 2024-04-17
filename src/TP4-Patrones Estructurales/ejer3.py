from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    def __init__(self, name: str) -> None:
        self._name = name

    def operation(self) -> str:
        return f"Leaf {self._name}"


class Composite(Component):
    def __init__(self, name: str) -> None:
        self._name = name
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite {self._name} [{', '.join(results)}]"


if __name__ == "__main__":

    producto_principal = Composite("Producto Principal")

    subconjunto_1 = Composite("Subconjunto 1")
    subconjunto_2 = Composite("Subconjunto 2")
    subconjunto_3 = Composite("Subconjunto 3")

    producto_principal.add(subconjunto_1)
    producto_principal.add(subconjunto_2)
    producto_principal.add(subconjunto_3)

    for i in range(1, 5):
        subconjunto_1.add(Leaf(f"Pieza {i}"))
        subconjunto_2.add(Leaf(f"Pieza {i+4}"))
        subconjunto_3.add(Leaf(f"Pieza {i+8}"))

    print("Configuracion del ensamblado:")
    print(producto_principal.operation())

    subconjunto_opcional = Composite("Subconjunto Opcional")

    for i in range(1, 5):
        subconjunto_opcional.add(Leaf(f"Pieza {i+12}"))

    producto_principal.add(subconjunto_opcional)

    print("Configuracion actualizada del ensamblado con subconjunto opcional:")
    print(producto_principal.operation())
