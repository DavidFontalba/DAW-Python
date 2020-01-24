# Programa para convertir minutos en horas:minutos:segundos
# Autor: David Galván Fontalba
# Fecha: 10/10/2019
#
# Algoritmo
#
#Pedir minutos
#Cálculo: 
#	hh <-- minutos//60
#	mm <-- ((minutos/60)-(hh))*60
#	ss <-- (mm - int(mm)*60)
#Muestro resultado

print("Bienvenido a este programa que transformará los minutos que insertes al formato: horas:minutos:segundos")
print("-------------------------------------------------------------------------------------------------------\n")

#Usuario inserta minutos
minutos = float(input("Inserte un valor numérico para los minutos a transformar: "))

#Cálculos
hh = minutos//60
mm = ((minutos/60)- hh)*60
ss = (mm - int(mm))*60

#Resultado en pantalla
print("--------------------------------------------------------------\n")
print(minutos, "minutos en formato 'horas:minutos:segundos' es:", int(hh),":",int(mm),":",int(ss))
