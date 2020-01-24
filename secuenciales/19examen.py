# Programa para calcular la nota de un examen en el que las respuestas correctas dan 5 puntos, las incorrectas restan 1, y las no contestadas 0
# Autor: David Galván Fontalba
# Fecha: 12/10/2019
#
# Algoritmo
# Pido respuestas correctas, incorrectas y respondidas en blanco
# Calculo 
# nota <-- correctas * 5 + incorrectas * (-1) + blanco * 0
# Muestro el resultado

print("Bienvenido a este programa para calcular tu nota")
print("------------------------------------------------\n")

#Pido datos
correctas = int(input("Inserta el número de respuestas correctas....: "))
incorrectas = int(input("Inserta el número de respuestas falladas.....: "))
blanco = int(input("Inserta el número de respuestas sin responder: "))

#Calculo la nota
nota = correctas * 5 - incorrectas
diez = (correctas + incorrectas + blanco)*5
notasobrediez = round((nota * 10) / diez, 2)
#Muestro el resultado
print("------------------------------------------------\n")
print(f"Has sacado un {notasobrediez} en el examen, por haber obtenido {nota} de {diez} puntos")
