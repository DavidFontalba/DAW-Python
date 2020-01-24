"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

Autor: David Galván Fontalba
Fecha: 26/10/2019

Algoritmo:
Pido la base y el exponente, establezco i y end(empieza con el valor de la base) como variables para calcular
    Mientras que i sea menor o igual a exponente
    i += 1
    end *= base
muestro el resultado
"""
print("Bienvenido a este programa para calcular una potencia.")
print("------------------------------------------------------\n")

#Pido base y exponente
base = float(input("Inserta un valor numérico para la base: "))
exponente = int(input("Inserta un valor numérico para el exponente: "))

#Establezco las variables para calcular
i = 1
end = base

#Calculo la potencia
while i < exponente:
    i += 1
    end *= base
print(f"¡El resultado de tu potencia es {end}")