"""
(c) UADER-FCyT-IS2 2024. Todos los derechos reservados.

Este programa lee un archivo JSON y extrae el valor de una clave especifica.
Utiliza el patrón de diseño Singleton para asegurar que solo haya una instancia
de la clase JsonReaderSingleton.

"""
import json
import sys

class JsonReaderSingleton:
    """
    Clase Singleton para leer una clave de un archivo JSON.
    """
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
        JsonReaderSingleton._instance = self

    def read_json_key(self, jsonfile, jsonkey):
        """Lee el archivo JSON y devuelve el valor de la clave especificada."""
        try:
            with open(jsonfile, 'r', encoding='utf-8') as myfile:
                data = myfile.read()
            obj = json.loads(data)
            return str(obj[jsonkey])
        except FileNotFoundError:
            return f"Error: El archivo {jsonfile} no existe."
        except KeyError:
            return f"Error: La clave '{jsonkey}' no se encontró en el archivo JSON."
        except json.JSONDecodeError:
            return "Error: El archivo JSON no es válido."
        except Exception as e:
            return f"Error inesperado: {str(e)}"

def main():
    """Función principal que maneja la ejecución desde la linea de comandos."""
    if len(sys.argv) < 2:
        print("Uso: python getJason_RE.py <archivo_json> <clave> o python getJason_RE.py -v")
        sys.exit(1)

    if sys.argv[1] == "-v":
        print("versión 1.1")
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Uso: python getJason_RE.py <archivo_json> <clave>")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    reader = JsonReaderSingleton.get_instance()
    result = reader.read_json_key(jsonfile, jsonkey)
    print(result)

if __name__ == "__main__":
    main()