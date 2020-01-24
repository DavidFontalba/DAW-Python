"""
Realiza un algoritmo que calcule la potencia, para ello pide por teclado
la base y el exponente. Pueden ocurrir tres cosas:

El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente 
positivo.

Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo:
Pido al usuario una potencia, dividida en dos variables: base y exponente
Si es positivo inserto la potencia, si el exponente es 0 el resultado es 1
y si el exponente es negativo el resultado será uno entre la potencia con
el exponente positivo
"""
print("Bienvenidos a este programa para calcular una potencia.")
print("-------------------------------------------------------\n")

# Pido la base y el exponente
base = float(input("Inserta la base de la potencia.....: "))
exp = float(input("Inserta el exponente de la potencia: "))

# Calculo el resultado en función
if exp > 0 :
    print("El resultado de la potencia es", base ** exp)
elif exp < 0 :
    print("El resultado de la potencia es", 1 / (base ** abs(exp)))
else :
    print("El resultado de la potencia es 1")
