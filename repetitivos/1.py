"""
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el
introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
si se llega al limite de intentos te muestra el número que había generado.

Autor: David Galván Fontalba
Fecha: 22/10/2019

Algoritmo:
Generar un número aleatorio entero del 1 al 100 <- numRandom
pido un número <- numGuess
mientras que numRandom y numGuess sean distintos y tenga intentos
    muestro si numRandom es menor o mayor que numGuess y resto un intento (empiezas con 10) y lo muestro
si se acierta el número, te dice en cuántos intentos lo has acertado.
si llegas al limite de intentos muestra numRandom
"""
import random

print("Bienvenido a este programa que consiste en que adivines un número generado aleatoriamente.")
print("------------------------------------------------------------------------------------------\n")

#Genero un número aleatorio
numRandom = random.randint(1, 100)
numGuess = -1
#Establezco los intentos de inicio por defecto
tries = 10
while numGuess != numRandom and tries != 0 :
    tries -= 1
    #Pido un número al usuario
    numGuess = int(input("Introduce un valor numérico entero entre el 1 y el 100, adivina en cuál estoy pensando: "))
    if numGuess <= 0 or numGuess >= 101 :
        print("El número tiene que estar entre 1 y 100.")
    elif numGuess < numRandom :
        print("Pienso en un número mayor.")
    elif numGuess > numRandom :
        print("Pienso en un número menor.")

    if tries != 1 :
        print(f"Te quedan {tries} intentos.\n")
    elif tries == 1 :
        print(f"Te queda {tries} intento.\n")

if tries == 0 :
    print(f"Lo siento\nEl número era {numRandom}, otra vez será.")
elif numGuess == numRandom :
    print("¡Correcto!\n")
    if tries != 1 :
        print(f"Aún tenías {tries} intentos.")
    elif tries == 1 :
        print(f"Te quedaba {tries} intento.")
