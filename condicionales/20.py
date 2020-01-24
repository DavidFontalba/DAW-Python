"""
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se
basa en el peso del paquete y la zona a la que va dirigido.

Lo anterior se muestra en la tabla:
ZONA	UBICACIÓN	        COSTO/GRAMO
1	    América del Norte	24.00 euros
2	    América Central	    20.00 euros
3	    América del Sur	    21.00 euros
4	    Europa	            10.00 euros
5	    Asia	            18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
esto por cuestiones de logística y de seguridad. 
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso,
el rechazo de la entrega.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
Pido los datos del peso en gramos y la zona a la que va dirigido
En función de la zona escogida calcular el precio y mostrar el resultado
1 <-- weight * 24
2 <-- weight * 20
3 <-- weight * 21
4 <-- weight * 10
5 <-- weight * 18
"""

print("Bienvenido a este programa para calcular el costo del servicio de transporte.")
print("-----------------------------------------------------------------------------\n")

# Pido los datos
zone = int(input(f"1 --- América del Norte.\n2 --- América Central.\n3 --- América del Sur.\n4 --- Europa.\n5 --- Asia.\n\nInserta un valor numérico para la zona de envío: "))
weight = float(input("Inserta un valor numérico en gramos para el peso del paquete a enviar: "))
print("----------------------------------------------------------------------------------\n")
# Compruebo la zona y muestro el resultado
if weight > 5000 :
    print(f"Lo lamentamos, por las condiciones de la empresa su paquete excede el peso admitido y no puede ser enviado.")
elif weight <= 0 :
    print(f"Para realizar un envío la cantidad tiene que ser mayor que cero.")
elif zone == 1 :
    print(f'El precio del paquete será de {round(weight*24, 2)} euros.')
elif zone == 2 :
    print(f'El precio del paquete será de {round(weight*20, 2)} euros.')
elif zone == 3 :
    print(f'El precio del paquete será de {round(weight*21, 2)} euros.')
elif zone == 4 :
    print(f'El precio del paquete será de {round(weight*10, 2)} euros.')
elif zone == 5 :
    print(f'El precio del paquete será de {round(weight*18, 2)} euros.')
else :
    print("Has introducido un número de zona no válido.")
