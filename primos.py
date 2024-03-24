# Python program to display all the prime numbers within an interval
#Intervalo de numeros 
#limite inferior
lower = 1
#limite superior
upper = 100
#imprime la leyenda "los numeros primos comprendidos son:"
print("Prime numbers between", lower, "and", upper, "are:")


for num in range(lower, upper + 1):
   # Todos los numeros primos mayores que 1 
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break #Sale del bucle si el numero no es primo
       else:
           print(num) #Imprime el número si es primo