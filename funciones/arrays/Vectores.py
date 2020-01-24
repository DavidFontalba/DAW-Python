import random

'''
* Ejercicios 20 - 28
* Crea una biblioteca de funciones para arrays (de una dimensión) de números
* enteros que contenga las siguientes funciones:
*
* 1. generaArrayInt: Genera un array de tamaño n con números aleatorios
* cuyo intervalo (mínimo y máximo) se indica como parámetro.
* 2. minimoArrayInt: Devuelve el mínimo del array que se pasa como parámetro.
* 3. maximoArrayInt: Devuelve el máximo del array que se pasa como parámetro.
* 4. mediaArrayInt: Devuelve la media del array que se pasa como parámetro.
* 5. estaEnArrayInt: Dice si un número está o no dentro de un array.
* 6. posicionEnArray: Busca un número en un array y devuelve la posición
* (el índice) en la que se encuentra.
* 7. volteaArrayInt: Le da la vuelta a un array.
* 8. rotaDerechaArrayInt: Rota n posiciones a la derecha los números de un
* array.
* 9. rotaIzquierdaArrayInt: Rota n posiciones a la izquierda los números de
* un array.
*
* @ author David Galván Fontalba
* Fecha: 08 / 12 / 2019
'''


'''
* 1. generaArrayInt: Genera un array de tamaño n con números aleatorios
* cuyo intervalo (mínimo y máximo) se indica como parámetro.
* @ param n
* @ param min
* @ param max
* @ return vector
'''


def generaArrayInt (n, min, max):
    vector = []
    for i in range(n):
        vector.append(random.randint(min, max))
    return vector


'''
* 2. minimoArrayInt: Devuelve el mínimo del array que se pasa como parámetro.
* @ param vector
* @ return min
'''


def minimoArrayInt (vector):
    min = vector[0]
    for i in range(len(vector)):
        if vector[i] < min:
            min = vector[i]
    return min


'''
* 3. maximoArrayInt: Devuelve el máximo del array quese pasa como parámetro.
* @ param vector
* @ return max
'''


def maximoArrayInt (vector):
    max = vector[0]
    for i in range(len(vector)):
        if vector[i] > max:
            max = vector[i]
    return max


'''
* 4. mediaArrayInt: Devuelve la media del array que se pasa como parámetro.
* @ param vector
* @ return media
'''


def mediaArrayInt(vector):
    sumatorio = 0
    for i in range(len(vector)):
        sumatorio += vector[i]
    media = sumatorio / len(vector)
    return media


'''
* 5. estaEnArrayInt: Dice si un número está o no dentro de un array.
* @ param num
* @ param vector
* @ return boolean
'''


def estaEnArrayInt(num, vector):
    for i in range(len(vector)):
        if num == vector[i]:
            return True
    return False


'''
* 6. posicionEnArray: Busca un número en un array y devuelve la posición
* (el índice) en la que se encuentra.
* @ param num
* @ param vector
* @ return
'''


def posicionEnArray(num, vector):
    for i in range(len(vector)):
        if num == vector[i]:
            return i
    return -1


'''
* 7. volteaArrayInt: Le da la vuelta a un array.
* @ param vector
* @ return vectorInverso
'''


def volteaArrayInt(vector):
    vectorInverso = []
    for i in range(len(vector)):
        vectorInverso.append(vector[((len(vector) - 1) - i)])
    return vectorInverso

'''
* 8. rotaDerechaArrayInt: Rota n posiciones a la derecha los números de un array.
* @ param n
* @ param vector
* @ return vectorRotadoDerecha
'''


def rotaDerechaArrayInt(n, vector):
    vectorRotadoDerecha = []
    for i in range(n):
        vectorRotadoDerecha.append(vector[len(vector) - n + i])
    for i in range(len(vector)-n):
        vectorRotadoDerecha.append(vector[i])
    return vectorRotadoDerecha


'''
* 9. rotaIzquierdaArrayInt: Rota n posiciones a la izquierda los números de un array.
* @ param n
* @ param vector
* @ return vectorRotadoDerecha
'''


def rotaIzquierdaArrayInt(n, vector):
    vectorRotadoIzquierda = []
    for i in range(len(vector)-n):
        vectorRotadoIzquierda.append(vector[n + i])
    for i in range(n):
        vectorRotadoIzquierda.append(vector[i])
    return vectorRotadoIzquierda
