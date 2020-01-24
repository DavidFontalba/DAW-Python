"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
pido cuantos números quiero introducir <-- cicles
mientras que cicles sea distinto a 0
    cicles pierde 1
    inserta un número <-- userNum
    depende de usernum añado +1 a un contador de mayor que cero, otro para menor que cero y otro para igual a cero
muestro los tres contadores
"""
print("Bienvenido a este programa para agrupar números que introduzcas en mayores, menores e iguales a cero.")
print("-----------------------------------------------------------------------------------------------------\n")

#Establezco los contadores en 0
zeroCount = 0
plusCount = 0
minusCount = 0
#Pido ciclos
cicles = int(input("¿Cuántos números vas a introducir?\n"))
#Pido números y voy contando
while cicles != 0 :
    cicles -= 1
    userNum = float(input("Introduce un número: "))
    if userNum < 0 :
        minusCount += 1
    elif userNum > 0 :
        plusCount += 1
    else :
        zeroCount +=1
print(f"\nHas introducido:\nNúmeros mayores que 0: {plusCount}\nNúmeros menores que 0: {minusCount}\nNúmeros iguales a 0..: {zeroCount}")