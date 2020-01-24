# Programa para hacer una media entre tres números
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
#
# Pido tres números a, b y c.
# Cálculo de la media
# Muestro el resultado
#
print("Bienvenidos a este programa que hará la media de tres números")
print("-------------------------------------------------------------\n")

#Pedimos los números
a = float(input("Dame el primer número: "))
b = float(input("Dame el segundo número: "))
c = float(input("Dame el tercer número: "))

#Cálculo
media = (a+b+c)/3

#Mostramos el resultado
print("--------------------------\n")
print("La media obtenida es:", media)
