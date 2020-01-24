# Programa para calcular la nota final de la asignatura Algoritmos con los porcentajes 
#    55% del promedio de sus tres calificaciones parciales.
#    30% de la calificación del examen final.
#    15% de la calificación de un trabajo final.
# Autor: David Galván Fontalba
# Fecha: 11/10/2019
#
# Algoritmo
# Pido las tres calificaciones, la del examen final y la del trabajo.
# Calculo 
#   calificaciones * 0.55 + examen final * 0.3 + trabajo * 0.15
#Muestro el resultado

print("Bienvenido a este programa para calcular tu nota en la asignatura Algoritmos")
print("----------------------------------------------------------------------------\n")

#Pido los datos
parcial1 = float(input("Introduce con un valor numérico la nota de tu primer parcial.: "))
parcial2 = float(input("Introduce con un valor numérico la nota de tu segundo parcial: "))
parcial3 = float(input("Introduce con un valor numérico la nota de tu tercer parcial.: "))
final = float(input("Introduce con un valor numérico la nota de tu examen final...: "))
trabajo = float(input("Introduce con un valor numérico la nota de tu trabajo final..: "))

#Cálculo
total = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + final * 0.3 + trabajo * 0.15

#Muestro el resultado
print("----------------------------------------------------------------------------\n")
print("Tu nota final en la asignatura de Algoritmos es un", round(total, 2))
