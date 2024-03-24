import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


def calcular_factoriales(rango):
    
    if "-" not in rango:
        inicio = 1
        fin = int(rango)
    
    elif rango.startswith("-"):
        inicio = 1
        fin = int(rango[1:])
    
    elif rango.endswith("-"):
        inicio = int(rango[:-1])
        fin = 60
    
    else:
        inicio, fin = map(int, rango.split('-'))
    
    for num in range(inicio, fin + 1):
        print("Factorial de", num, "! es", factorial(num))        


if len(sys.argv) < 2:
    print("Si no se coloca alguno de los limites los preterminados seran inicio=1, fin=60")
    rango = input("ingrese el rango de numeros en el formato 'desde-hasta': ")
else:
    rango=sys.argv[1]

calcular_factoriales(rango)