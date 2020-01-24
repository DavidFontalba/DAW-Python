"""
Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
sustituye la aparición del primer carácter en la cadena por el segundo carácter.

Autor: David Galván Fontalba
Fecha: 28/10/2019

Algoritmo:
Pido una cadena y dos carácteres, si es más de un carácter se lo vuelvo a pedir,
y distintos, si los pusiera igual, se los vuelvo a pedir
creo una auxiliar i para el bucle
creo una cadena que sera el resultado
mientras i sea menor que la longitud de la cadena
    si el caracter en posicion i es igual al primer caracter
        el caracter en posicion i de nuestra frase será sumo a la nueva frase el segundo caracter
    si no
        sumo a la nueva frase el caracter en posicion i
muestro el resultado
"""
print("Bienvenido a este programa para sustituir un carácter que aparezca en una frase por otro distinto.")
print("--------------------------------------------------------------------------------------------------\n")

#Pido los datos
ourString = input("Inserta la cadena a la que le quieres cambiar un carácter: ")

#Pido los caracteres, validando que son solo 1 y que son distintos, porque si son iguales la solución es la misma
charOne = "aa"
charTwo = "aa"

while charOne == charTwo : #Para que sean caracteres distintos
    while len(charOne) != 1 : #Para que me introduzca un solo carácter
        charOne = input("Introduce un carácter, será aquel que quieres quitar: ")
        if len(charOne) != 1 :
            print("Tiene que ser un solo carácter.\n")
    while len(charTwo) != 1 :
        charTwo = input("Introduce un carácter, será aquel por el que quieres sustituir: ")
        if len(charTwo) != 1 :
            print("Tiene que ser un solo carácter.\n")
    if charOne == charTwo :
        print("Si los carácteres son el mismo, el resultado es la frase que has insertado.\n")
        print("Tienen que ser distintos, vuelve a introducirlos.\n")

#Empiezo el bucle,
#mientras i sea menor que la longitud de la cadena
#cada vez que el caracter en posición i sea igual a el caracter 
#uno cambiamos el caracter en esa posición por el dos

i = 0
newString = ""
while i < len(ourString):
    if ourString[i] == charOne:
        newString += charTwo
    else: 
        newString += ourString[i]
    i += 1

#Muestro el resultado
print(f"La frase, cambiando el carácter '{charOne}' por el carácter '{charTwo}' es:\n{newString}")