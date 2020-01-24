# Programa para transformar grados Fahrenheit a grados Celsius
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
# 
# Pido grados Fahrenheit
# Cálculo celsius <-- (fah - 32) / (9/5)
# Muestro los grados Celsius
print("Bienvenido a este programa para convertir grados Fahrenheit a grados Celsius")
print("----------------------------------------------------------------------------\n")

#Pido grados
fah = float(input("Dame un valor numérico que sean los grados Fahrenheit que quieres convertir: "))

#Cálculos
celsius = (fah-32)/(9/5)

#Muestro
print(fah,"º Fahrenheit son:", celsius,"º Celsius")
