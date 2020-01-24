# Programa para decirte el total de euros y céntimos que tienes cuándo le insertes la cantidad de monedas
# Autor: David Galván Fontalba
# Fecha: 12/10/2019
#
# Algoritmo
# Pido monedas
# Calculo 
# total en centimos <- 2e*200 + 1e*100 + 50c*50 + 20c*20 + 10c*10
# separo euros y centimos
# Muestro el resultado

print("Bienvenido a este programa para sumar monedas")
print("---------------------------------------------\n")

#Pido las monedas
eu2 = int(input("¿Cuántas monedas de 2 euros tienes?     "))
eu1 = int(input("¿Cuántas monedas de 1 euro tienes?      "))
ce50 = int(input("¿Cuántas monedas de 50 céntimos tienes? "))
ce20 = int(input("¿Cuántas monedas de 20 céntimos tienes? "))
ce10 = int(input("¿Cuántas monedas de 10 céntimos tienes? "))

#Calculo
totalcent = eu2*200 + eu1*100 + ce50*50 + ce20*20 + ce10*10
#Divido en euros y céntimos
euros = totalcent/100
centimos = (totalcent/100 - totalcent//100)*100

#Muestro el resultado
print("---------------------------------------------\n")
print(f"Con esas monedas juntas un total de {int(euros)} euros y {round(centimos)} céntimos")
