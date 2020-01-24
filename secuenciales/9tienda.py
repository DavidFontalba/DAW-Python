# Programa para averiguar cuanto tendras que pagar si te descuentan un 15%
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
# Pido cuánto se ha gastado en total comprando
# Calculo el precio con el descuento aplicado
# Muestro el resultado

print("Bienvenido a este programa para aplicarle un 15% de descuento a tu compra y saber cuánto valdrá")
print("-----------------------------------------------------------------------------------------------\n")

# Pido el dato
compra = float(input("Introduce, usando un valor numérico, y en euros, cuánto vale el total de tu compra: "))

# Cálculos
total = compra - (compra * 0.15)

# Muestro el resultado
print("-----------------------------------------------------------------------------------------------\n")
print("Con el descuento aplicado, ¡tan solo tendrás que pagar", total, "euros!")
