#Programa para averiguar cuánto cobrara en comisiones por separado, así como junto al resto del sueldo fijo.
#Autor: David Galván Fontalba
#Fecha: 10/10/2019
#
#Algoritmo
#Pido: sueldofijo, comision1, comision2 y comision3
#Cálculos. 
#   comisiones <-- 0.1*(comision1+comision2+comision3)
#   sueldototal <- sueldofijo+comisiones
#Muestro el resultado

print("Bienvenido a este programa para calcular tu sueldo")
print("--------------------------------------------------\n")

#Pido los datos
sueldofijo = float(input("Ingresa, con un valor numérico y en euros, tu sueldo fijo: "))
comision1 = float(input("Ingresa, con un valor numérico y en euros, el cobro de tu primera venta: "))
comision2 = float(input("Ingresa, con un valor numérico y en euros, el cobro de tu segunda venta: "))
comision3 = float(input("Ingresa, con un valor numérico y en euros, el cobro de tu tercera venta: "))

#Cálculos
comisiones = 0.1*(comision1+comision2+comision3)
sueldototal = sueldofijo + comisiones

#Resultado
print("--------------------------------------------------\n")
print("Esta ocasión vas a cobrar en comisiones un total de", round(comisiones, 2), "euros, y ganarás un sueldo total de", round(sueldototal, 2), "euros.")
