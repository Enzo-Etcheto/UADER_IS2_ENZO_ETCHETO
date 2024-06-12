"""
(c) UADER-FCyT-IS2 2024. Todos los derechos reservados.

Este programa gestiona pagos utilizando el patron de diseño Singleton y Chain of Responsibility.
"""
import json
import sys

class JsonReaderSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        """Devuelve la unica instancia de JsonReaderSingleton."""
        if JsonReaderSingleton._instance is None:
            JsonReaderSingleton()
        return JsonReaderSingleton._instance

    def __init__(self):
        """Constructor privado de la clase Singleton."""
        if JsonReaderSingleton._instance is not None:
            raise Exception("Esta clase es un Singleton. Use get_instance() para obtener la instancia.")
        else:
            JsonReaderSingleton._instance = self
            self.tokens = self._load_tokens()

    def _load_tokens(self):
        try:
            with open('sitedata.json', 'r') as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            raise Exception("Error: El archivo sitedata.json no existe.")
        except json.JSONDecodeError:
            raise Exception("Error: El archivo JSON no es valido.")
    
    def get_token_key(self, token_name):
        """Devuelve la clave asociada al token."""
        try:
            return self.tokens[token_name]
        except KeyError:
            raise Exception(f"Error: El token '{token_name}' no se encontro en el archivo JSON.")

class Cuenta:
    def __init__(self, token_name, saldo_inicial):
        self.token_name = token_name
        self.saldo = saldo_inicial
        self.token_key = JsonReaderSingleton.get_instance().get_token_key(token_name)

    def procesa_pago(self, monto):
        """Verifica si la cuenta puede procesar el pago."""
        return self.saldo >= monto

    def procesar_pago(self, monto):
        """Procesa el pago si hay suficiente saldo."""
        if self.procesa_pago(monto):
            self.saldo -= monto
            return True
        return False

class Manejadorpagos:
    def __init__(self):
        self.cuentas = [Cuenta("token1", 1000), Cuenta("token2", 2000)]
        self.pagos = []

    def procesar_pago(self, orden_numero, monto):
        """Procesa un pago alternando entre las cuentas disponibles."""
        for cuenta in self.cuentas:
            if cuenta.procesar_pago(monto):
                self.pagos.append({
                    "orden_numero": orden_numero,
                    "token": cuenta.token_name,
                    "monto": monto
                })
                return f"Pedido {orden_numero}: Pago de ${monto} realizado con {cuenta.token_name}"
        return f"Pedido {orden_numero}: No se pudo realizar el pago. Fondos insuficientes."

    def listar_pago(self):
        """Devuelve una lista de todos los pagos realizados."""
        return self.pagos

class Iteradorpago:
    def __init__(self, pagos):
        self._pagos = pagos
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._pagos):
            pago = self._pagos[self._index]
            self._index += 1
            return pago
        raise StopIteration

def main():
    """Funcion principal que maneja la ejecucion desde la linea de comandos."""
    if len(sys.argv) < 2:
        print("Uso: python getJason_IR.py <archivo_json> <clave> o python getJason_IR.py -v")
        sys.exit(1)

    if sys.argv[1] == "-v":
        print("version 1.2")
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Uso: python getJason_IR.py <archivo_json> <clave>")
        sys.exit(1)

    jsonkey = sys.argv[2]

    lector = JsonReaderSingleton.get_instance()
    resultado = lector.get_token_key(jsonkey)
    print(resultado)

    # Gestion de pagos
    manejador = Manejadorpagos()
    print(manejador.procesar_pago(1, 500))
    print(manejador.procesar_pago(2, 500))
    print(manejador.procesar_pago(3, 500))
    print(manejador.procesar_pago(4, 500))
    print(manejador.procesar_pago(5, 500))

    # Listado de pagos realizados
    pagos = manejador.listar_pago()
    iterador = Iteradorpago(pagos)
    for pago in iterador:
        print(pago)

if __name__ == "__main__":
    main()