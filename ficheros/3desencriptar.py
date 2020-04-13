
import sys
import string

"""
3. Haz un programa que reciba como parámetro un fichero encriptado con el método César y y almacene el resultado en otro, que también pasamos como parámetro, de manera que:

Si el programa no recibe dos parámetros termina con un error 1.
Si el programa recibe un solo parámetro guardará la información desencriptada en el mismo archivo del que lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Para desencriptar necesitas una clave que debes pedir al usuario.
¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave? Coméntala, y si te atreves... ¡impleméntala!
@author David Galván Fontalba
@version 1.0
"""

"""
MÉTODOS
"""


def cesar_decrypt(line, displacement):
    """
    Encripta una cadena que recibe como parámetro
    :param line:
    :param displacement:
    :return: decrypted_line
    """
    decrypted_line = ""
    for character in line:
        if character in string.ascii_letters:
            character_is_in_pos = string.ascii_letters.index(character)
            decrypted_character_is_in = (character_is_in_pos - displacement) % len(string.ascii_letters)
            if decrypted_character_is_in < 0:
                decrypted_character = string.ascii_letters[len(string.ascii_letters) + decrypted_character_is_in]
            else:
                decrypted_character = string.ascii_letters[decrypted_character_is_in]
        else:
            decrypted_character = character
        # añadimos a la cadena
        decrypted_line += decrypted_character

    return decrypted_line


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
        resp = input("¿Continuar? (S/N) ").upper()
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

# Pedimos desplazamiento para desencriptar usando el método César
while True:
    try:
        displacement = input("Elige el desplazamiento para desencriptar o introduce Z para probar automáticamente: ")
        int(displacement)
    except ValueError:
        if displacement.upper() != "Z":
            print("Dato incorrecto. Introduce un valor entero.")
        else:
            break
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


# Escribir fichero desencriptado
if displacement.upper() != "Z":
    for line in origin:
        final_driver.write(cesar_decrypt(line, int(displacement)))
    final_driver.close()

    #V.0.1 --> Mejorable para que no te pregunte en cada iteración si está bien o no.
else: #Probamos a desencriptar automaticamente
    displacement = 1
    while True:


        for line in origin:
            print(cesar_decrypt(line, int(displacement)))

        while True: # Pido si continuar probando o escribir la información
            resp = input("¿Es correcto el desencriptado? (S/N) ").upper()
            if resp == "S":
                break
            if resp == "N":
                displacement += 1
                break

        if resp == "S":
            break

    for line in origin:
        final_driver.write(cesar_decrypt(line, int(displacement)))
    final_driver.close()

