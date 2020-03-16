
import sys
import string

"""
MÉTODOS
"""


def cesar_encrypt(line, displacement):
    """
    Encripta una cadena que recibe como parámetro
    :param line:
    :param displacement:
    :return: encrypted_line
    """
    encrypted_line = ""
    for character in line:
        if character in string.ascii_letters:
            is_in_pos = string.ascii_letters.index(character)
            encrypted_character_is_in = (is_in_pos + displacement) % len(string.ascii_letters)
            encrypted_character = string.ascii_letters[encrypted_character_is_in]
        else:
            encrypted_character = character
        # añadimos a la cadena
        encrypted_line +=  encrypted_character

    return encrypted_line


"""
PROGRAMA PRINCIPAL
"""
# Número de parámetros correcto
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Error en el número de parámetros", file=sys.stderr)
    exit(1)

# Averiguamos fichero origen y destino
origin_file = sys.argv[1]
if len(sys.argv) == 2:
    final_file = origin_file
    # El archivo se eliminará
    print("Solo ha indicado un nombre de archivo:", origin_file)
    print("Los datos de", origin_file, "serán eliminados.")
    while True:
        resp = input("¿Continuar? (S/N) ")
        if resp in ["S", "N"]:
            break
    if resp == "N":
        exit(0)
else:
    final_file = sys.argv[2]

# Abrimos fichero origen
try:
    origin_driver = open(origin_file, "r")
except FileNotFoundError: # Si el fichero no existe
    print("El fichero", origin_file, "no se ha podido abrir.")
    exit(2)

# Pedimos desplazamiento para encriptar usando el método César
while True:
    try:
        displacement = int(input("Elige el desplazamiento para encriptar: "))
    except ValueError:
        print("Dato incorrecto. Introduce un valor entero.")
    else:
        break

# Leemos fichero origen
origin = origin_driver.readlines()
origin_driver.close()

# Abrimos fichero a encriptar
try:
    final_driver = open(final_file, "w")
except PermissionError or FileNotFoundError: # Si el fichero no existe
    print("El fichero", origin_file, "no se ha podido abrir.")
    exit(2)

# Escribir fichero encriptado
for line in origin:
    final_driver.write(cesar_encrypt(line, displacement))
final_driver.close()