# Programa para escribir las iniciales, ingresados por el usuario nombre y apellidos.
# Autor: David Galván Fontalba
# Fecha: 12/10/2019
#
# Algoritmo
# Pido nombre y apellidos.
# Creo una cadena que serán las iniciales
# Muestro el resultado

print("Bienvenido a este programa para escribir las iniciales de un nombre, ingresados por el usuario nombre completo y apellidos")
print("--------------------------------------------------------------------------------------------------------------------------\n")

#Pido las variables
nombre = input("Inserta un nombre..........: ")
apellido = input("Inserta un primer apellido.: ")
apellido2 = input("Inserta un segundo apellido: ")

#Creo el resultado
iniciales = (nombre.title()[0] + "." + apellido.title()[0] + "." + apellido2.title()[0] + ".")

#Muestro el resultado
print("--------------------------------------------------------------------------------------------------------------------------\n")
print("Las iniciales del nombre que has ingresado son", iniciales)
