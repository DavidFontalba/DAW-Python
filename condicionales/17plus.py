"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un 
dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
Pido el número inicial
Muestro el resultado según el número introducido por el usuario
------------------------------------------------------------------
A modo de repaso de cara al examen voy a introducir un menú para elegir realizar el ejercicio en sí (decir el lado opuesto)
o escoger la opción " No tengo dado :( ", que generará un número aleatorio del 1 al 6, en este caso se mostrará otro menú
con las opciones "a) Mostrar el lado opuesto" y "b) Volver al inicio"

Algoritmo:
Muestro el menú
A) Insertar cara opuesta <-- Pido el número inicial
B) No tengo dado :( <-- Genero un número aleatorio usando la funcion randint() y lo muestro
    B) limpia la pantalla y abre otro menú donde las opciones son
        a) Mostrar el lado opuesto <-- hace lo mismo que A) pero sin que el usuario tenga que insertar nada
        b) Cerrar <-- el programa se cierra
Muestro el resultado según el número introducido por el usuario o generado automaticamente
"""
import random
import os
import sys

print("Bienvenido a este programa para decirte la cara opuesta de un dado de seis caras.")
print("---------------------------------------------------------------------------------\n")
# Menu AB
print("A ) Insertar cara opuesta")
print("B ) No tengo dado :(")
firstElection = input("Escoge una opción: ")

if firstElection == "A" or firstElection == "a" : #Si escribe A
    number = int(input("Introduce un valor numérico para el número obtenido en el dado: ")) # Pido el número que quiera introducir

elif firstElection == "B" or firstElection == "b" : #Si escribe B
    if os.name == "posix": # Limpio pantalla
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    number = random.randint(1, 6)
    print(f'Te ha salido un "{number}"\n')
    # Menu ab
    print("a ) Mostrar el lado opuesto") 
    print("b ) Cerrar programa")
    secondElection = input("Escoge una opción: ")

    if secondElection == "b" or secondElection == "B" : #Si escribe b
        sys.exit()
    elif secondElection != "a" and secondElection != "A" : #Si no escribe a ni b
        print("No has introducido una opción válida")
        sys.exit()
        
else: #Si no escribe una opción válida
    print("No has introducido una opción válida.")
    sys.exit()
# Muestro el resultado de la cara opuesta
if number == 1 :
    print("La cara opuesta de tu número es el seis.")
elif number == 2 :
    print("La cara opuesta de tu número es el cinco.")
elif number == 3 :
    print("La cara opuesta de tu número es el cuatro.")
elif number == 4 :
    print("La cara opuesta de tu número es el tres.")
elif number == 5 :
    print("La cara opuesta de tu número es el dos.")
elif number == 6 :
    print("La cara opuesta de tu número es el uno.")
else :
    print("ERROR: número incorrecto.")