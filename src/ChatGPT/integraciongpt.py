#Integracion con API de OpenAI- Enzo Etcheto

import os
import sys
from openai import OpenAI

#Se carga la API-KEY atraves del archivo .env
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Crear el cliente de OpenAI
client = OpenAI(
    api_key=API_KEY
)

#Buffer para almacenar las consultas
consulta_buffer=[]

def obtener_ultima_consulta():
    """Funcion para optener la ultima consulta"""
    if consulta_buffer:
        return consulta_buffer[-1]

def main():
    """Funcion que desarrolla la conexicon con la API"""
    #Se verifica si el modo conversacion esta activo
    modo_conversacion = "--convers" in sys.argv

    while True:
        try:
            #Se lee la consulta
            if sys.stdin.isatty():  # verifica si la cosulta esta en la terminal
                consulta_usuario = input("Ingrese su consulta: ")
                if consulta_usuario.strip() == "":
                    print("La consulta no puede estar vacía.")
                    continue
            else:
                #Si la entrada no esta conectada a la terminal, se usa la ultima consulta
                consulta_usuario = obtener_ultima_consulta()

            #Se verifica si esta en modo conversacion y se agrega la consulta al buffer
            if modo_conversacion and consulta_usuario.strip() != "":
                consulta_buffer.append(consulta_usuario)

            #Se construye el contexto para la API
            context = ""
            if consulta_buffer:
                context = consulta_buffer[-1]

            #Llamado a la API de chatGPT
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": context,
                    },
                    {
                        "role": "user",
                        "content": consulta_usuario,
                    }
                ]
            )

            #Imprimir la respuesta de chatGPT
            respuesta_texto = response.choices[0].message["content"]
            print("chatGPT:", respuesta_texto)

            #Agregar la respuesta al buffer si la convercacion esta activa
            if modo_conversacion:
                consulta_buffer.append(respuesta_texto)

        #Si se pone Ctrl+C se interrumpe el programa
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break
        except Exception as e:
            print("Se ha producido un error:", e) #Indica si se a producido un error

#Permite determinar si el script está siendo ejecutado directamente o si está siendo importado como un módulo.
if __name__ == "__main__":
    main()
