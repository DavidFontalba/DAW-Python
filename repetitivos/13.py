"""
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

Autor: David Galván Fontalba
Fecha: 28/10/2019

Algoritmo:
Pido una frase
variable auxiliar i que irá incrementando en 1 por ciclo
creo una variable que sera la nueva frase
mientras i sea menor que la longitud de nuestra frase
    si el caracter número (i, para que vaya incrementando y comprobando cada vez un carácter) es igual a el caracter i en mayusculas
        sumo el caracter i en minusculas a la nueva frase
    si no
        sumo el caracter i en mayusculas a la nueva frase
muestro el resultado
"""
print("Bienvenido a este programa para cambiar las mayúsculas y minúsculas de una frase por su contraria.")
print("--------------------------------------------------------------------------------------------------\n")

#Pido la frase
ourString = input("Inserta una frase: ")

#Creo una variable auxiliar i con valor cero y empiezo el bucle
i = 0
newString = ""
while i < len(ourString):
    if ourString[i] == ourString.upper()[i]:
        newString += ourString.lower()[i]
    else:
        newString += ourString.upper()[i]
    i += 1
print(f"\nEl resultado es:\n{newString}")