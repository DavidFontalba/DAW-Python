"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Autor: David Galván Fontalba
Fecha: 26/10/2019

Algoritmo:
pido dos numeros
    para i en el rango entre los dos números
    muestro los numeros con el modulo de 2 == 0
fin
"""
print("Bienvenido a este programa para decirte todos los números pares entre dos números.")
print("----------------------------------------------------------------------------------\n")

#Pido los números
start = int(input("Inserta un primer número para establecer el inicio del rango: "))
end = int(input("Inserta un segundo valor para establecer el final del rango: "))

#Crear un bucle asignandole a i cada valor del rango
for i in range(start, end+1):
    if i%2 == 0: #Solo muestro los números pares en nuestro rango
        print(i)

print("\n¡Ya está! ¡Hasta pronto!")