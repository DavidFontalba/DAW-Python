"""
Construcción de la clase fecha
"""
from Fecha import Fecha, FechaErronea

# Construir una fecha
dia = int(input("Día para construir una fecha: "))
mes = int(input("Mes para construir una fecha: "))
anyo = int(input("Año para construir una fecha: "))

fecha = Fecha(anyo, mes, dia)

print("La fecha introducida es: ", fecha)