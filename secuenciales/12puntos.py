# Programa para medir la distancia entre dos puntos
# Autor: David Galván Fontalba
# Fecha: 11/10/2019
#
# Algoritmo
# Pido dos puntos, cuatro coordenadas
# Calculo 
#  Raiz cuadrada de (x2-x1)^2+(y2-y1)^2
# Muestro el resultado
import math

print("Bienvenido a este programa para medir la distancia entre dos puntos")
print("-------------------------------------------------------------------\n")

#Pido los puntos
x1 = float(input("Dame la primera coordenada, x, del primer punto.: "))
y1 = float(input("Dame la segunda coordenada, y, del primer punto.: "))
x2 = float(input("Dame la primera coordenada, x, del segundo punto: "))
y2 = float(input("Dame la segunda coordenada, y, del segundo punto: "))

#Cálculo
distancia = abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

#Muestro resultados
print("-------------------------------------------------------------------\n")
print("La distancia entre el punto", "(" + str(x1) + "," + str(y1) + ")", "y el punto", "(" + str (x2) + "," + str(y2) + ")", "es: ", round(distancia, 2))
