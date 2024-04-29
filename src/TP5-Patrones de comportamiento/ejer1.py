from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
    
class ManejadorNumero(ABC):

    @abstractmethod
    def set_next(self, handler: ManejadorNumero) -> ManejadorNumero:
        pass

    @abstractmethod
    def manejar_numero(self, numero: int) -> Optional[str]:
        pass

class ManejadorNumeroAbstracto(ManejadorNumero):

    _siguiente_manejador: ManejadorNumero = None

    def set_next(self, handler: ManejadorNumero) -> ManejadorNumero:
        self._siguiente_manejador = handler
        return handler

    def manejar_numero(self, numero: int) -> Optional[str]:
        if self._siguiente_manejador:
            return self._siguiente_manejador.manejar_numero(numero)
        return None

class ManejadorNumerosPrimos(ManejadorNumeroAbstracto):


    def es_primo(self, numero: int) -> bool:
        if numero <= 1:
            return False
        if numero <= 3:
            return True
        if numero % 2 == 0 or numero % 3 == 0:
            return False
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

    def manejar_numero(self, numero: int) -> Optional[str]:
        if self.es_primo(numero):
            return f"{numero} es consumido por el ManejadorNumerosPrimos"
        else:
            return super().manejar_numero(numero)

class ManejadorNumerosPares(ManejadorNumeroAbstracto):

    def manejar_numero(self, numero: int) -> Optional[str]:
        if numero % 2 == 0:
            return f"{numero} es consumido por el ManejadorNumerosPares"
        else:
            return super().manejar_numero(numero)

class ConsumidorNumeros:

    def __init__(self, manejador: ManejadorNumero):
        self._manejador = manejador

    def consumir_numeros(self) -> None:
        for numero in range(1, 101):
            resultado = self._manejador.manejar_numero(numero)
            if resultado:
                print(resultado)
            else:
                print(f"{numero} no fue consumido.")

if __name__ == "__main__":
    manejador_primos = ManejadorNumerosPrimos()
    manejador_pares = ManejadorNumerosPares()

    manejador_primos.set_next(manejador_pares)

    consumidor = ConsumidorNumeros(manejador_primos)
    consumidor.consumir_numeros()
