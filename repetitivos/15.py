"""
Introducir una cadena de caracteres e indicar si es un palíndromo.
Una palabra palíndroma es aquella que se lee igual adelante que atrás.

Autor: David Galván Fontalba
Fecha: 28/10/2019

Algoritmo:
Pido una cadena
creo una variable i igual a cero
otra variable igual a la longitud de la cadena <-- range
una variable que será nuestra nueva cadena
mientras range mayor o igual a cero:
    si el caracter en posicion i de la cadena es igual al de posicion range 
        i mas uno
        range menos uno
        nueva cadena mas el caracter en posicion i
if nueva cadena es igual a cadena
    muestro el resultado afirmativo
si no
    muestro el negativo
"""
print("Bienvenido a este programa para comprobar si una cadena es palíndroma.")
print("----------------------------------------------------------------------\n")

#Pido una cadena
ourString = input("Inserta una cadena: ")

#Creo variables auxiliares
i = 0
rangeString = len(ourString) - 1
firstString = ""
secondString = ""

#Voy creando cadenas, en dos variables auxiliares, una de izq a derecha y otra al contrario,
#cuando i y el rango sean iguales, será el último carácter necesario comprobar,
#por si el número de carácteres es impar
while i <= rangeString and ourString[i] == ourString[rangeString] :
    firstString += ourString[i]
    secondString += ourString[rangeString]
    i += 1
    rangeString -= 1

#Muestro si es palindromo o no
if firstString == secondString and firstString != "" :
    print("\nLa cadena es palíndroma.")
else:
    print("\nLa cadena no es palíndroma.")