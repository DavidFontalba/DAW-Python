# Programa para saber a qué hora llega un ciclista de una ciudad A a otra B.
# Autor: David Galván Fontalba
# Fecha: 12/10/2019
#
# Algoritmo
# Pido la hora y el tiempo en segundos que tarda en llegar.
# Calculo 
# Convierto la hora a segundos, le sumo los que ha tardado y convierto el total en la nueva hora
# Muestro el resultado

print("Bienvenido a este programa para averiguar a qué hora llegará un ciclista que sale de una ciudad A a una hora y tarda T segundos en llegar a una ciudad B")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

#Pido las variables
print("¿Qué hora era cuando el ciclista salió de la primera ciudad?")
hh = int(input("Horas...: "))
mm = int(input(f"Minutos.: {hh}:"))
ss = int(input(f"Segundos: {hh}:{mm}:"))
print("\n""¿Cuántos segundos tardó en llegar?")
t = int(input())
#Calculo
sstotal = (hh*3600 + mm*60 + ss) + t
#Convierto los segundos totales a horas, minutos, segundos
hhfin = sstotal//3600
mmfin = ((sstotal/3600)- hhfin)*60
ssfin = (mmfin - int(mmfin))*60

#Muestro el resultado
print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")
hora = str(int(hhfin)) + ":" + str(int(mmfin)) + ":" + str(int(ssfin))
print("El ciclista llegará a la ciudad B a las", hora)
