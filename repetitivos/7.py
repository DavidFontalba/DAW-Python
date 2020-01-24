"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.

Autor: David Galván Fontalba
Fecha: 22/10/2019

Algoritmo:
price <-- 10
i <-- 1
month <-- pedir mes que quiere averiguar (1-20)
mientras i < month
    price * 2
"""

#Pido qué més quiere averiguar
month = 0
while month < 1 or month > 20 :
    month = int(input("Inserta un valor numérico para el precio del mes que quieres saber (Del 1 al 20): "))
    if month < 1 or month > 20 :
        print("Inserta un número válido\n")

#Establezco unas variables
price = 10 #Lo que paga el primer mes
i = 0
total = 0 #Para ir calculando el total
for i in range(1, 21) :
    total += price #Sumo el precio en cada ciclo para calcular el total de los 20 meses
    if i == month : #Para especificarle el precio en el mes concreto
        print(f"Este mes tendrás que pagar {price} euros.")
    price *= 2 #Cada mes se duplica el precio

print(f"En total habrás pagado {total} euros.")