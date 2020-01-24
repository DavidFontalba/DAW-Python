"""
Escribe un programa que pida un número entero entre uno y doce 
e imprima el número de días que tiene el mes correspondiente.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
Pido un número del 1 al 12 para el mes
los meses 1,3,5,7,8,10,12 tienen 31 días
los meses 4,6,9,11 tienen 30 días
el mes 2 tiene 28 días
Muestro el resultado al comprobar de qué mes se trata
"""

print("Bienvenido a este programa para saber el número de días que tiene un mes.")
print("-------------------------------------------------------------------------\n")

# Pido el número del mes
monthNumber = int(input("Introduce un valor numérico para el mes (del 1 al 12): "))


# Muestro el resultado correspondiente
thirtyOne = monthNumber == 1 or monthNumber == 3 or monthNumber == 5 or monthNumber == 7 or monthNumber == 8 or monthNumber == 10 or monthNumber == 12
thirty = monthNumber == 4 or monthNumber == 6 or monthNumber == 9 or  monthNumber == 11

if thirtyOne :
    print(f'\nEl mes "{monthNumber} tiene 31 días')
elif thirty :
    print(f'\nEl mes "{monthNumber}" tiene 30 días')
elif monthNumber == 2 : #Febrero
    print(f'\nEl mes "2" tiene 28 días ')
else:
    print(f'\nERROR: El número "{monthNumber}" no es válido.')