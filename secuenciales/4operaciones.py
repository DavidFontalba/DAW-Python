# Programa que hace una suma, una resta, una división y una multiplicación dados dos números
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
#
# Pido dos números a y b
# Calculamos
# Mostramos los distintos resultados
#
print("Bienvenido, este programa realizará una suma, una resta, una división y una multiplicación con los números que me des")
print("---------------------------------------------------------------------------------------------------------------------\n")

#Pedimos los números
a = float(input("Dame un primer número:  "))
b = float(input("Dame un segundo número: "))

#Cálculos
suma = a + b
resta = a - b
division = a / b
multiplicacion = a * b

#Mostramos
print("--------------------")
print("Para", a, "+", b, "=", suma)
print("Para", a, "-", b, "=", resta)
print("Para", a, "/", b, "=", division)
print("Para", a, "*", b, "=", multiplicacion)
