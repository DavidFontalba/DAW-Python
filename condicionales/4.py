"""
Crea un programa que pida al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrario.
Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo:
Pedimos dos números
Los números los dividiremos si el divisor no es 0 y mostraremos el 
resultado, y si lo es avisaremos de que no se puede realizar la operación.
"""
print("Bienvenidos a este programa para dividir dos números, si el segundo toma de valor 0, no se podrá realizar la operación.")
print("-----------------------------------------------------------------------------------------------------------------------\n")

# Pedir números
a = float(input("Inserta un primer valor numérico.: "))
b = float(input("Inserta un segundo valor numérico: "))

# Si b no es cero, dividimos y mostramos el resultado, si no mostramos un mensaje de error.
if b != 0 :
    print("El resultado de la división es: ", round(a/b, 3))
else :
    print("Has insertado un 0 para el divisor, por tanto no se puede llevar a cabo la división")
