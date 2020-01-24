"""
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
circunferencias y las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas

Autor: David Galván Fontalba
Fecha: 18/10/2019

Algoritmo:
Pido las variables de los puntos y radios de la circunferencia 1 y después de la 2
Creo una variable para la distancia entre dos puntos <-- Raiz cuadrada de (x2-x1)^2+(y2-y1)^2
Compruebo en qué estado clasificar las circunferencias

exteriores              <-- Distancia entre los centros mayor que la suma de sus radios
tangentes exteriores    <-- La suma de los radios es igual a la distancia de los centros
secantes                <-- Distancia entre los centros menor que la suma de sus radios
tangentes interiores    <-- Distancia entre los centros es igual que la diferencia de sus radios
interiores              <-- Distancia entre los centros es menor que la diferencia de las longitudes de sus radios
concéntricas            <-- El mismo centro pero distintos radios
"""
import math

print("Bienvenido a este programa para clasificar el estado de dos circunferencias")
print("---------------------------------------------------------------------------\n")

# Pido los centros y los radios
x1 = float(input("Inserta un valor númerico para la coordenada x de la primera circunferencia: "))
y1 = float(input("Inserta un valor númerico para la coordenada y de la primera circunferencia: "))
r1 = float(input("Inserta un valor númerico para el radio de la primera circunferencia.......: "))

x2 = float(input("Inserta un valor númerico para la coordenada x de la segunda circunferencia: "))
y2 = float(input("Inserta un valor númerico para la coordenada y de la segunda circunferencia: "))
r2 = float(input("Inserta un valor númerico para el radio de la segunda circunferencia.......: "))

# Asigno una variable que calcula la distancia entre dos números
dist = abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

# Compruebo el estado y en función al resultado se lo muestro al usuario

if dist > (r1 + r2):
    print("Las circunferencias son exteriores.")

elif dist < (r1 + r2) and dist > abs(r1 - r2):
    print("Las circunferencias son secantes.")

elif dist < abs(r1 - r2):
    print("Las circunferencias son interiores.")

elif dist == (r1 + r2):
    print("Las circunferencias son tangentes exteriores.")

elif dist == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores.")

elif x1 == x2 and y1 == y2 and r1 != r2 :
    print("Las circunferencias son concéntricas.")

else :
    print("Las circunferencias no pueden ser clasificadas en ninguno de los estados de este programa.")
