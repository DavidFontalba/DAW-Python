"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y
‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce
un espacio

Autor: David Galván Fontalba
Fecha: 22/10/2019

Algoritmo:
doy un valor cualquiera a userChar
mientras userChar sea distinto a un espacio
    pido insertar userChar
    si es a, e, i, o, u
        imprimir 'VOCAL'
    si no
        imprimir ' NO VOCAL'
"""
print("Bienvenido a este programa para decirte si los carácteres que introduces son vocales o no.")
print("------------------------------------------------------------------------------------------\n")
print("Inserta un espacio en cualquier momento para salir del programa.\n")

#Establezco la variable userChar
userChar = "A"
while userChar != " " : #Bucle hasta que escriba espacio para salir
    #Pido carácter
    userChar = input("Inserta 1 carácter: ") 
    if len(userChar) != 1 :
        print("Solo debes introducir un carácter.")
    #vocal
    elif userChar == "a" or userChar == "A" or userChar == "e" or userChar == "E" or userChar == "i" or userChar == "I" or userChar == "o" or userChar == "O" or userChar == "u" or userChar == "U" :
        print("'VOCAL'")
    #Salida
    elif userChar == " ": 
        print("¡Nos vemos pronto!")
    #no vocal
    else :
        print("'NO VOCAL'")