"""
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), 
realiza un programa que cuente cuantas palabras tiene.

Autor: David Galván Fontalba
Fecha: 28/10/2019

Algoritmo:
Pido una frase
Establezco un contador con valor 1 por la primera palabra
variable auxiliar i que irá incrementando en 1 por ciclo
mientras i sea menor que la longitud de nuestra frase
    si el caracter número (i, para que vaya incrementando y comprobando cada vez un carácter) es un espacio
        añadir +1 al contador
    sumo i y termino el bucle
muestro el resultado
"""
print("Bienvenido a este programa para que introduzcas una frase, y decirte cuántas palabras tiene.")
print("--------------------------------------------------------------------------------------------\n")

#Pido la frase
ourString = input("Escribe una frase: ")

#El contador empieza como 1 por la primera palabra de las frases
counter = 1

#Empiezo el bucle, cada vez que halla 1 espacio se sumará al contador
#el bucle se realizará tantas veces como carácteres tenga la frase
i = 0
while i < len(ourString) :
    if ourString[i] == " " : #Usaré el carácter espacio para contar la separación de palabras
        counter += 1
    i += 1

#Muestro el resultado final
print(f"\nLa frase tiene {counter} palabras.")