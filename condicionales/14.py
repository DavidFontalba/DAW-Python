"""
La asociación de vinicultores tiene como política fijar un precio 
inicial al kilo de uva, la cual se clasifica en tipos A y B, y 
además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta 
es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un 
productor por la uva que entrega en un embarque, considerando lo siguiente:
 
si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es 
de tamaño 1 y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan
30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. 
Realice un algoritmo para determinar la ganancia obtenida.

Autor: David Galván Fontalba
Fecha: 21/10/2019

Algoritmo:
Pedir cuántos kilos de uva, el precio por kilo, qué tipo y qué tamaño
A y t1 <-- +20 centimos
A y t2 <-- +30 centimos
B y t1 <-- -30 centimos
B y t2 <-- -50 centimos
Hacer los cálculos en función de a qué tipos y tamaños pertenecen
y mostrar el resultado al usuario

Considero que la carga del precio se suma (o resta) por kilo, y no al total
"""
print("Bienvenido vinicultor, en este programa podrás calcular el precio total de tus uvas en función de su tipo y tamaño.")
print("-------------------------------------------------------------------------------------------------------------------")

# Pido los datos
kofGrapes = float(input("Inserte cuántos kilos de uva quieres vender....: "))
pricePerK = float(input("Inserta, en céntimos, el precio del kilo de uva: "))
grapeType = input("Inserta el tipo de uva (A o B).................: ")
grapeSize = int(input("Inserta el tamaño de la uva (1 o 2)............: "))

# Hago los cálculos para las 4 combinaciones
grapeA1 = kofGrapes * (pricePerK + 20)
grapeA2 = kofGrapes * (pricePerK + 30)
grapeB1 = kofGrapes * (pricePerK - 30)
grapeB2 = kofGrapes * (pricePerK - 50)

# Muestro el resultado
if grapeType == "A" and grapeSize == 1 :
    print(f"El precio total será de {grapeA1}")
elif grapeType == "A" and grapeSize == 2 :
    print(f"El precio total será de {grapeA2}")
elif grapeType == "B" and grapeSize == 1 :
    print(f"El precio total será de {grapeB1}")
elif grapeType == "B" and grapeSize == 2 :
    print(f"El precio total será de {grapeB2}")
else:
    print("Reinicia el programa e inserta valores válidos.")
