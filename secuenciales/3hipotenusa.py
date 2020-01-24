# Programa que calcula la hipotenusa de un triángulo rectángulo dados sus catetos
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
#
# Leer los dos catetos
# hipotenusa <-- raiz cuadrada del (cateto1 ** 2 + cateto2 ** 2)
# Mostrar resultado
#
# Importamos math
import math

#Presentación
print("Bienvenido a este programa para calcular la hipotenusa de un triángulo rectángulo")
print("---------------------------------------------------------------------------------")

# Pedimos base y altura del triángulo
cateto1 = float(input("Dame un valor numérico para un cateto del triángulo: "))
cateto2 = float(input("Dame otro para el otro cateto: "))

# Cálculos
hipotenusa = math.sqrt((cateto1**2)+(cateto2**2))

# Mostramos el resultado
print("------------------------------------------------------")
print("La hipotenusa de tu triángulo es:", hipotenusa)
