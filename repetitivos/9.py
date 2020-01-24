"""
Mostrar en pantalla los N primeros número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

Autor: David Galván Fontalba
Fecha: 27/10/2019

Algoritmo:
Pido la cantidad de números primos que queremos mostrar.
Enseño el primero que siempre va a ser 2 y creo un contador
Empiezo a probar números, el primero será el 3
Mientras nuestro contador sea menor que la cantidad de números que buscamos haremos lo siguiente:
    Crearemos una variable para afirmar que es primo
    Otra variable para el divisor, empezará siendo 3 igual que el número con el que empezamos
    Mientras el divisor sea menor que la raiz cuadrada del numero que estamos intentando y la variable que afirma que es primo sigue siendo verdadera
        si el resto entre el numero y el divisor es cero es divisible, por tanto la variable que afirma que es primo será falsa
        sumamos dos al divisor para probar el siguiente divisor impar
    si hemos terminado el bucle anterior y la variable que afirma que es primo sigue siendo verdadera (hemos encontrado un número primo)
        añado 1 al contador y enseño el resultado
    Para probar si el siguiente número es primo, sumo 2 a la variable con la que estabamos probando (empezó siendo 3)
"""
print("Bienvenido a este programa para indicarte los X primeros números primos.")
print("------------------------------------------------------------------------\n")

#Pido datos
amount = int(input("Inserte la cantidad de números primos que quiere saber (Mínimo 1): "))

#El primer primo, y el único que es par va a ser dos
if amount >= 2 :
    print("El 1º número primo es: 2")

counter = 1

#Hago los calculos para el resto, los impares
tryingNumber = 3
while counter < amount :
    itsPrime = True #Suponemos que va a ser un número primo
    divider = 3 #El primer número que no es ni uno (porque va a salir siempre) ni dos (porque no va a ser par)
    while divider <= tryingNumber*(1/2) and itsPrime == True : #Mientras el divisor sea menor que la raíz cuadrada del número a comprobar y siga siendo primo (porque no hemos hayado que no lo es aún)
        if tryingNumber%divider == 0: #Si el resto da cero dejará de ser un candidato a ser primo
            itsPrime = False
        divider += 2 #Probamos con el siguiente divisor impar
    if itsPrime: #Si es primo
        counter += 1 #Añadimos uno a nuestro contador
        print(f"El {counter}º número primo es: {tryingNumber}") #Mostramos el resultado
    tryingNumber += 2 #Una vez terminado, probamos con el siguiente número impar.
