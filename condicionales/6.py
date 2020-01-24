"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo:
Pido al usuario una cadena
Compruebo que lo que el usuario ha introducido es UNA letra, y mayúscula
para ello comprobaremos que el primer carácter de la cadena es igual a
la cadena entera <-- len(cadena) sera igual a 1, y posteriormente que sea
mayor o igual que A y menor o igual que Z
"""
print("Bienvenidos a este programa para que insertes una cadena y comprobar si es una letra mayúscula.")
print("-----------------------------------------------------------------------------------------------\n")

# Pedimos al usuario que inserte una cadena
cad = input("Escribe: ")

# Comprobamos que sea una sola letra y que además sea mayúscula
if len(cad) == 1 and (cad >= "A" and cad <= "Z") or cad == "Ñ" or cad == "Ü" or cad == "Ç" or (cad >= "Á" and cad <= "Ú") or (cad >= "À" and cad <= "Ù"):
    print("Has insertado una única letra mayúscula.")
else :
    print("No has insertado una única letra mayúscula.")
