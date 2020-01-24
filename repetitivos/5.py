"""
Escribe un programa que pida el limite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 

A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

Autor: David Galván Fontalba
Fecha: 26/10/2019

Algoritmo:
Pido un intervalo downLimit y upLimit <-- si downLimit > upLimit lo vuelvo a pedir
Pido que introduzca números hasta que escriba el 0 para parar.
Muestro al usuario: Suma de los números que ha introducido que esten dentro del intervalo
                    Cuántos números ha introducido pero están fuera del intervalo
                    Si ha introducido un número igual a los límites del intervalo
"""
print("Bienvenido a este programa donde establecerás un intervalo y después introduciras números.")
print("Te enseñaré la suma de los números que introduciste dentro del intervalo, cuántos están fuera, y cuántos en los límites.")
print("------------------------------------------------------------------------------------------------------------------------\n")

#Pido el intervalo
start = 3
end = 2
while start >= end :
    start = int(input("Inserta un primer número para establecer el límite inferior del intervalo: "))
    end = int(input("Inserta un segundo valor para establecer el límite superior del intervalo: "))
    if start >= end :
        print("El limite inferior tiene que ser menor que el superior.")

number = 1
counterSame = 0
counterOut = 0
sumIn = 0
while number != 0:
    number = int(input("Inserta un número, para terminar inserte el 0: "))
    if number == start or number == end :
        counterSame += 1
    elif number < start or number > end :
        counterOut += 1
    else: 
        sumIn += number

print(f"\n¡Has introducido {counterSame} números iguales a los límites, {counterOut} números fuera de los límites, y la suma de los números internos es: {sumIn}!")
print("\n¡Hasta pronto!")
