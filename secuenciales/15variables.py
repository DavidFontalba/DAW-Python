# Programa para intercambiar valores entre variables.
# Autor: David Galván Fontalba
# Fecha: 11/10/2019
#
# Algoritmo
# Pido las variables
# Calculo 
# Muestro el resultado

print("Bienvenido, definirás dos variables A y B y el programa intercambiará sus valores")
print("---------------------------------------------------------------------------------\n")

#Pido las variables
a = float(input("Variable a = "))
b = float(input("Variable b = "))

#Cálculo
c = a
a = b
b = c

#Muestro el resultado
print("---------------------------------------------------------------------------------\n")
print("Ahora a =", a, "y b =", b)
