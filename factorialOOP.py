class FactorialOOP:
    

    def __init__(self, min, max):
       
        self.min = min
        self.max = max

    def run(self):
    
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
    
        for num in range(self.min, self.max + 1):
            print("Factorial de", num, "! es", factorial(num))


min = int(input("Ingrese el numero minimo del rango: "))
max = int(input("Ingrese el numero maximo del rango: "))

factorial_obj = FactorialOOP(min, max)
factorial_obj.run()