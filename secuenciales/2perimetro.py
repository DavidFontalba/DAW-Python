# Programa para calcular el perímetro de un rectángulo
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
#
# Pedimos la base y la altura
# perimetro <-- 2 * (base + altura)
# Mostramos el resultado
#
print("Bienvenido a este programa con el que calcular el perímetro de un rectángulo")
print("----------------------------------------------------------------------------")
# Pedimos la base y la altura
base = float(input("Dame un valor numérico para la base: "))
altura = float(input("Ahora otro para la altura: "))

# Cálculos
perimetro = 2 * (base + altura)

# Solución en pantalla
print("El perimetro de un rectángulo de base", base, "y altura", altura, "es igual a: ", perimetro)
