"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
dimensiones de los lados de un triángulo. El programa debe determinar 
que tipo de triángulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Autor: David Galván Fontalba
Fecha: 19/10/2019

Algoritmo:
Pedimos tres números A, B y C que serán los lados de un triángulo
En función de los lados, determinar qué tipo de triángulo es y mostrarlo
al usuario
1. si tequilatero <-- 3 lados iguales
2. si no y, trectangulo <-- hipotenusa ** 2 == cateto1 ** 2 + cateto2 ** 2
3. si tisosceles <-- 2 lados iguales
4. si no, es escaleno <-- si no se cumple nada de lo otro
"""

print("Bienvenido a este programa para determinar el tipo de triángulo según los lados que insertes.")
print("---------------------------------------------------------------------------------------------\n")

# Pido los lados
a = float(input("Inserta un valor numérico para uno de los lados del triángulo........: "))
b = float(input("Inserta un valor numérico para otro de los lados del triángulo.......: "))
c = float(input("Inserta un último valor numérico para otro de los lados del triángulo: "))

# Compruebo las condiciones para clasificar el triángulo y muestro el
# resultado al usuario

isEquilateral = a == b == c
isIsosceles = a == b != c or a == c != b or b == c != a
isRight = a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2

if isEquilateral :
    print("El triángulo es equilátero.")
else:
    
    if isRight :
        print("El triángulo es rectángulo.")
    
    if isIsosceles :
        print("El triángulo es isósceles.")

    else: 
        print("El triángulo es escaleno.")
