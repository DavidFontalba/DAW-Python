"""
Realiza un programa que pida el día de la semana (del 1 al 7) y 
escriba el día correspondiente. Si introducimos otro número nos da un error.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
Pido el número del 1 al 7 para el dia de la semana
Muestro el resultado del día considerando el 1 como lunes y el 7 como domingo
"""

print("Bienvenido a este programa para convertir el número del día de la semana al nombre del día correspondiente.")
print("----------------------------------------------------------------------------------------------------------\n")

# Pido el número del día
dayNumber = int(input("Introduce un valor numérico para el día de la semana (del 1 al 7): "))

# Muestro el resultado correspondiente
if dayNumber == 1 :
    print(f"El día {dayNumber} corresponde al lunes")
elif dayNumber == 2 :
    print(f"El día {dayNumber} corresponde al martes")
elif dayNumber == 3 :
    print(f"El día {dayNumber} corresponde al miércoles")
elif dayNumber == 4 :
    print(f"El día {dayNumber} corresponde al jueves")
elif dayNumber == 5 :
    print(f"El día {dayNumber} corresponde al viernes")
elif dayNumber == 6 :
    print(f"El día {dayNumber} corresponde al sábado")
elif dayNumber == 7 :
    print(f"El día {dayNumber} corresponde al domingo")
else:
    print(f"ERROR: El número {dayNumber} no es válido.")