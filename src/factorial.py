import sys
def factorial(num): 
    #Si el numero es negativo, imprime que no se puede hacer factorial de un numero negativo 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    #Si el numero es 0, se retorna 1
    elif num == 0: 
        return 1
    #Si el numero es mayor que 0, se calcula el factorial    
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#Función para calcular los factoriales de un rango de numeros
def calcular_factoriales(rango):
    #Si no hay un guion en el rango, se interpreta como un solo numero
    if "-" not in rango:
        inicio = 1
        fin = int(rango)
    #Si el rango comienza con un guion, se calcula desde 1 hasta el numero
    elif rango.startswith("-"):
        inicio = 1
        fin = int(rango[1:])
    #Si el rango termina con un guion, se calcula desde el numero hasta 60
    elif rango.endswith("-"):
        inicio = int(rango[:-1])
        fin = 60
    #Si hay 1 guion en el rango, se interpretan como dos numeros
    else:
        inicio, fin = map(int, rango.split('-'))
    #Se recorre el rango y se calcula el factorial de cada numero
    for num in range(inicio, fin + 1):
        print("Factorial de", num, "! es", factorial(num))        

#Si no se ha especificado un rango en la terminal, se solicita 
if len(sys.argv) < 2:
    print("Si no se coloca alguno de los limites los preterminados seran inicio=1, fin=60")
    rango = input("ingrese el rango de numeros en el formato 'desde-hasta': ")
else:
    rango=sys.argv[1]
#Se calcula el factorial del rango 
calcular_factoriales(rango)