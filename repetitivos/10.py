"""
Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

Autor: David Galván Fontalba
Fecha: 27/10/2019

Algoritmo:
Pido un cadena
Pido un caracter
contador en 0
Hago una variable que empieza siendo 0, i
mientras i <= len(cadena)
    si cadena[i] == caracter
        contador +1
    si no
        i +1
fin
"""
print("Bienvenido a este programa para que introduzcas una frase y un carácter, y decirte cuántas veces aparece ese carácter en tu frase.")
print("----------------------------------------------------------------------------------------------------------------------------------\n")

ourString = input("Escribe lo que quieras: ")
ourChar = input("Escribe un solo carácter: ")

counter = 0
i = 0
while i < len(ourString) :
    if ourString[i] == ourChar :
        counter += 1
    i += 1
print(f"\nEl carácter {ourChar} aparece {counter} veces.")