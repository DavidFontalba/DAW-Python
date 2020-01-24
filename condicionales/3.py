"""
Escribe un programa que lea un número e indique si es par o impar.
Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo:
Pedimos un número, si la división entera entre 2 y la división normal entre 2 es igual será par.
Comprobamos si el número es par
"""
print("Bienvenidos a este programa para saber si un número es par o impar.")
print("-------------------------------------------------------------------\n")

# Pedir número
a = float(input("Inserta un número: "))

# Comprobamos si es par o impar y mostramos el resultado
if a/2 == a//2 :
    print("El número que has ingresado es par.")
else :
    print("El número que has ingresado es impar.")
