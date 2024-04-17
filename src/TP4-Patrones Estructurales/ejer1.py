import subprocess
from abc import ABC, abstractmethod

class Ping(ABC):
    @abstractmethod
    def ejecutar(self, direccion: str) -> None:
        pass

    def ejecutar_libre(self, direccion: str) -> None:
        print(f"Haciendo ping a {direccion} sin verificar la IP...")
        for _ in range(10):
            resultado = subprocess.run(['ping', '-c', '1', direccion], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if resultado.returncode == 0:
                print(f"Exito: {direccion} es alcanzable")
            else:
                print(f"Fallo: {direccion} no es alcanzable")

class PingReal(Ping):
    def ejecutar(self, direccion: str) -> None:
        if not direccion.startswith("192."):
            print("La direccion debe comenzar con '192.'")
            return
        print(f"Haciendo ping a {direccion}...")
        for _ in range(10):
            resultado = subprocess.run(['ping', '-c', '1', direccion], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if resultado.returncode == 0:
                print(f"Exito: {direccion} es alcanzable")
            else:
                print(f"Fallo: {direccion} no es alcanzable")

class ProxyPing(Ping):
    def __init__(self, ping_real: PingReal) -> None:
        self._ping_real = ping_real

    def ejecutar(self, direccion: str) -> None:
        if direccion == "192.168.0.254":
            print("Usando el metodo libre de ejecucion para la direccion '192.168.0.254'")
            self._ping_real.ejecutar_libre("www.google.com")
        else:
            self._ping_real.ejecutar(direccion)

if __name__ == "__main__":
    ping_real = PingReal()
    proxy_ping = ProxyPing(ping_real)

    proxy_ping.ejecutar("192.168.1.1")
    proxy_ping.ejecutar("192.168.0.254")
    proxy_ping.ejecutar("8.8.8.8")
