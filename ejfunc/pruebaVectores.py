import funciones.arrays.Vectores

'''
*Para probar que las funciones realizadas funcionan
*
* @ author David Galván Fontalba
* Fecha: 08 / 12 / 2019
'''


arrayPrueba = funciones.arrays.Vectores.generaArrayInt(10, 1, 10)
print("Array generado")
for element in arrayPrueba:
    print(element, end=" ")

print("\nMínimo")
print(funciones.arrays.Vectores.minimoArrayInt(arrayPrueba))

print("Máximo")
print(funciones.arrays.Vectores.maximoArrayInt(arrayPrueba))

print("Media")
print(funciones.arrays.Vectores.mediaArrayInt(arrayPrueba))

print("esta en array 1, 3, 5")
print(funciones.arrays.Vectores.estaEnArrayInt(1, arrayPrueba))
print(funciones.arrays.Vectores.estaEnArrayInt(3, arrayPrueba))
print(funciones.arrays.Vectores.estaEnArrayInt(5, arrayPrueba))

print("posicion en array")
print(funciones.arrays.Vectores.posicionEnArray(1, arrayPrueba))
print(funciones.arrays.Vectores.posicionEnArray(3, arrayPrueba))
print(funciones.arrays.Vectores.posicionEnArray(5, arrayPrueba))

print("Voltea")
arrayVolteado = funciones.arrays.Vectores.volteaArrayInt(arrayPrueba)
for element in arrayVolteado:
    print(element, end=" ")

print("\nRota derecha")
arrayRotDer = funciones.arrays.Vectores.rotaDerechaArrayInt(3, arrayPrueba)
for element in arrayRotDer:
    print(element, end =" ")

print("\nRota izquierda")
arrayRotIzq = funciones.arrays.Vectores.rotaIzquierdaArrayInt(3, arrayPrueba)
for element in arrayRotIzq:
    print(element, end=" ")