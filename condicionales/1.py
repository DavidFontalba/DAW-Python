"""
Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo
Pedir dos números, a y b.
Comparar los dos números y afirmar o negar si el primero es mayor.
"""
print("Bienvenidos a este programa para saber, entre dos números, si el primero es mayor al segundo.")
print("---------------------------------------------------------------------------------------------\n")

# Pedir números
a = float(input("Introduce el primer número.: "))
b = float(input("Introduce el segundo número: "))

# Comparamos los números y mostramos el resultado en función del resultado de la comparación
if a > b :
    print("El primer número es mayor que el segundo.")
elif b > a :
    print("El primer número no es mayor que el segundo, es menor.")
else :
    print("El primer número no es mayor que el segundo, es igual.")
