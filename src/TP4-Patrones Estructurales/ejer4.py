from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def operation(self) -> int:
        pass


class Number(Component):

    def __init__(self, value: int) -> None:
        self._value = value

    def operation(self) -> int:
        return self._value


class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> int:
        return self._component.operation()


class SumaDecorator(Decorator):
    def operation(self) -> int:
        return self._component.operation() + 2


class MultiplicarDecorator(Decorator):
    def operation(self) -> int:
        return self._component.operation() * 2


class DividirDecorator(Decorator):
    def operation(self) -> int:
        return self._component.operation() / 3


def client_code(component: Component) -> None:

    print(f"RESULT: {component.operation()}")


if __name__ == "__main__":
    numero = Number(10)
    print("Numero original:")
    client_code(numero)

    decorated_numero = SumaDecorator(numero)
    print("Numero despues de sumar 2:")
    client_code(decorated_numero)

    decorated_numero = MultiplicarDecorator(numero)
    print("Numero despues de multiplicar por 2:")
    client_code(decorated_numero)

    decorated_numero = DividirDecorator(numero)
    print("Numero despues de dividir por 3:")
    client_code(decorated_numero)

    combinado_decorator = DividirDecorator(MultiplicarDecorator(SumaDecorator(numero)))
    print("Numero despues de sumar 2, multiplicar por 2 y dividir por 3:")
    client_code(combinado_decorator)