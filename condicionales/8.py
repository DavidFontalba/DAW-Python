"""
Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el 
mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a 
dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe 
imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo:
Pido que el usuario inserte las variables nota, edad y sexo
Compruebo las variables y muestro los resultados en función de los requisitos
para nota mayor o igual a cinco, edad mayor o igual a 18 y sexo F será ACEPTADA
para nota mayor o igual a cinco, edad mayor o igual a 18 y sexo M será POSIBLE
si no se cumplen las condiciones será NO ACEPTADA
"""
print("Bienvenidos a este programa para comprobar si has sido aceptada, posible o no aceptada.")
print("---------------------------------------------------------------------------------------\n")

# Pido las variables
note = float(input("Inserta tu nota: "))
age = float(input("Inserta tu edad: "))
gender = input("Inserta tu sexo ('F' para femenino o 'M' para masculino): ")

# Compruebo los requisitos y muestro el resultado
if note >= 5 and age >= 18 and gender == 'F' :
    print("ACEPTADA")
elif note >= 5 and age >= 18 and gender == 'M' :
    print("POSIBLE")
else :
    print("NO ACEPTADA")
