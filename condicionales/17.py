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
"""

print("Bienvenido a este programa para decirte la cara opuesta de un dado de seis caras.")
print("---------------------------------------------------------------------------------\n")
# Pido el número que quiera introducir
number = int(input("¿Qué número ha salido en el dado?\n")) 

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
    print(f'ERROR: El número "{number}" es incorrecto.')