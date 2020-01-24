# Programa para invertir las posiciones de un número de dos cifras
# Autor: David Galván Fontalba
# Fecha: 11/10/2019
#
# Algoritmo
# Pido el número
# Calculo 
# Muestro el resultado

print("Bienvenido a este programa invertir las posiciones de un número de dos cifras")
print("-----------------------------------------------------------------------------\n")

#Pido el número
numero = int(input("Dame un número de dos cifras: "))

#Cálculo
inverso = str(numero - (int(numero*0.1)*10)) + str(int(numero*0.1))

#Muestro el resultado
print("-----------------------------------------------------------------------------\n")
print("El número invertido de", numero, "es", int(inverso))
