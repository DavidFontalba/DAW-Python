"""
Escribir un programa que lea un e año indicar si es bisiesto. Nota: un 
año es bisiesto si es un número divisible por 4, pero no si es divisible 
por 100, excepto que también sea divisible por 400.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
Pedimos el año
Comprobamos si es divisible por 4, en ese caso
comprobamos que no sea divisible por cien pero si por 400
Entonces sera bisiesto, sino no.
"""
print("Bienvenido a este programa para comprobar si un año es bisiesto o no.")
print("---------------------------------------------------------------------\n")

# Pido el año
year = int(input("Inserte un valor numérico para el año: "))

# Hacemos las comprobaciones
if year/4 == year//4 :
    if year/100 != year//100 or year/400 == year//400 :
        print(f"El año {year} es bisiesto.")
else :
    print(f"El año {year} no es bisiesto.")
