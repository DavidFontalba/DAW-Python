"""
Realizar un programa que compruebe si una cadena contiene una subcadena.
Las dos cadenas se introducen por teclado.

Autor: David Galván Fontalba
Fecha: 28/10/2019

Algoritmo:
Pido la cadena y una subcadena
creo dos auxiliares, aux e i, y una nueva cadena para comprobar al final
mientras i sea menor que la longitud de la cad 1 y aux menor que la longitud de la cad 2
    si la posicion i de la cad 1 es igual a la posicion aux de la cad 2
        concateno la posicion i de la cadena 1 a nuestra nueva cadena
        sumo 1 a auxiliar
    sumo 1 a i
compruebo si la nueva cadena es igual a la subcadena e imprimo el resultado
"""
print("Bienvenido a este programa para comprobar si una cadena contiene a otra subcadena.")
print("----------------------------------------------------------------------------------\n")

#Pido las cadenas
ourString = input("Inserta la cadena grande, que tendrá o no en su interior a la otra:\n")
subString = input("\nInserta otra cadena que estará o no en la cadena anterior:\n")

#Creo variables auxiliares
aux = 0
i = 0
newString = ""

#Empiezo el bucle
while i < len(ourString) and aux < len(subString): #Para evitar errores en el calculo, si i o aux llega al limite de la cadena para.
    if ourString[i] == subString[aux]:
        newString += ourString[i]
        aux += 1
    i += 1

#Muestro el resultado
if newString == subString:
    print("La segunda cadena está dentro de la primera.")
else:
    print("La segunda cadena no está dentro de la primera.")