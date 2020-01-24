# Programa para medir la distancia entre dos números
# Autor: David Galván Fontalba
# Fecha: 11/10/2019
#
# Algoritmo
# Pido dos números
# Calculo 
#   Valor absoluto de a - b
# Muestro el resultado

print("Bienvenido a este programa para medir la distancia entre dos puntos")
print("-------------------------------------------------------------------\n")

#Pido los números
a = float(input("Inserte un primer número: "))
b = float(input("Inserte otro número más.: "))

#Calculo la distancia
distancia = abs(a-b)

#Muestro el resultado
print("-------------------------------------------------------------------\n")
print("La distancia entre", a, "y", b, "es:", distancia)
