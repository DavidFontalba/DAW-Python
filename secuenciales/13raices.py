# Programa para calcular la raíz cuadrada y la raíz cúbica de un número
# Autor: David Galván Fontalba
# Fecha: 11/10/2019
#
# Algoritmo
# Pido el número
# Calculo 
#  Calculo la raiz cuadrada, y para la raiz cubica <-- x ** (1/3)
# Muestro el resultado
import math

print("Bienvenido a este programa para calcular la raíz cuadrada y la raíz cúbica de un número")
print("---------------------------------------------------------------------------------------\n")

#Pido el número
x = float(input("Dame un número: "))

#Calculos
r2 = math.sqrt(x)
r3 = x ** (1/3)

#Muestro el resultado
print("---------------------------------------------------------------------------------------\n")
print("La raíz cuadrada de", x, "es:", round(r2, 3), "\ny su raíz cúbica es.......:", round(r3, 3))
