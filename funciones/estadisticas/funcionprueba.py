"""
Ejemplo de librería de funciones dentro de un paquete
"""
def charRepeat(caracter='-', repeticion=3):
    print(caracter * repeticion)

def funcion1():
    print("Soy func1")

def funcion2(param):
    print("soy func2 y tengo ", param)

def funcion3(*param):
    print(f"Soy la func3 y me has llamado con {len(param)} parametros")
    for p in range(len(param)):
        print(f"Parametro {p}")