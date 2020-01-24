# Programa para saber cuántos minutos tardará un vehiculo en alcanzar a otro, teniéndo en cuénta que el de atrás irá más rápido.
# Autor: David Galván Fontalba
# Fecha: 12/10/2019
#
# Algoritmo
# Pido la distancia, la velocidad del de atrás, y la del primero.
# Calculo 
# tiempomin <-- (distancia/(velocidad1-velocidad2))*60
# Muestro el resultado

print("Bienvenido a este programa para averiguar cuánto tardará un vehículo X que va más rápido y por detrás de otro vehículo Y")
print("------------------------------------------------------------------------------------------------------------------------\n")

#Pido las variables
velocidad1 = float(input("Inserta un valor en km/h para la velocidad del vehículo, X, que va detrás...............: "))
velocidad2 = float(input("Inserta un valor en km/h para la velocidad del primer vehículo, Y, menor que la anterior: "))
distancia = float(input("Inserta una valor en km para la distancia que separa ambos vehículos....................: "))

#Cálculo
tiempomin = (distancia/(velocidad1-velocidad2))*60

#Muestro el resultado
print("------------------------------------------------------------------------------------------------------------------------\n")
print("El vehículo X alcanzará al Y en", round(tiempomin, 2), "minutos.")
