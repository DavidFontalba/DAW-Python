"""
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.

Autor: David Galván Fontalba
Fecha: 26/10/2019

Algoritmo:
Pido cuanto quiere contar
establezco ahora en 0
empiezo un bucle que durara hasta que ahora y la variable antes pedida sean iguales
    contador
    convertidor de segundos y los muestro

"""
import time

future = int(input("Inserta cuántos segundos quieres contar: "))
now = 0

while now < future :
    now = time.perf_counter()
    seconds = int(now)
    hourEnd = seconds//3600
    minEnd = (seconds/3600 - hourEnd)*60
    secEnd = (minEnd - int(minEnd))*60
    print(f"{int(hourEnd)}:{int(minEnd)}:{int(secEnd)}")
