import sys
import requests
import os

"""
PROGRAMA PRINCIPAL

1. Usando esta API de OpenWeather que nos da el pronóstico del tiempo para una ciudad que se le pide al usuario de los
siguientes cinco días, mostrar:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.
Tened en cuenta que las respuestas de esta api referentes a los días y horas usan el tiempo en formato UNIX (UTC).

1. Modifica el ejercicio 1 del tema anterior de manera que:

El programa admita dos parámetros:
El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la ciudad es errónea el programa 
termina con un mensaje de error y código 2.
El segundo es opcional, y si existe, es el directorio donde vamos a crear un fichero html con la información formateada 
como una tabla del pronóstico de la temperatura, si no existe la información se muestra por pantalla. 

Consideraciones:
este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, 
ejemplo: "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de error (código 1) diciendo 
que la sintaxis es incorrecta.
Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto explicando qué hace.

@author David Galván Fontalba
@version 2
"""
# Métodos
def show_help():
    """
    Muestra la sintaxis de este programa y su funcionalidad.
    """
    print("Este programa nos da el pronóstico del tiempo de los próximos cinco días para una ciudad.\n")
    print("Sintaxis: python3 ej01_tiempo_en_5_dias.py {CIUDAD} [{DIRECTORIO}]\n")
    print("Si {DIRECTORIO} no se especifica la información se muestra por la pantalla, si se hace se genera un fichero "
          + "html en DIRECTORIO con nombre {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}.\n")
    print("Si {DIRECTORIO} se especifica hay que añadir al final del nombre / (Unix/Linux) ó \\ (Windows).")


def request_to_json(city):
    """
    Consulta en la API de Open Weather el pronóstico del tiempo para los próximos cinco días.
    :param city: Localidad para que la hacemos la consulta.
    :return: JSON con las mediciones del tiempo (40)
    """
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": os.environ["OPENWEATHER_ID"], "units": "metric", "lang": "es"}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error al hacer la petición o", city, "no existe:", response.status_code, file=sys.stderr)
        exit(2)
    return response.json()


def temp_calcs(days, totals, data):
    """
    Calcula las temperaturas media, máxima y mínima diarias, y la global.
    :param days: lista donde guardamos los datos diarios.
    :param totals: diccionario donde guardamos los datos globales.
    :param data: JSON con los datos devueltos con la API de OpenWeathers
    """
    for content in data["list"]:
        # fecha y temperatura de la medición
        day = content["dt_txt"][:10]
        temp = float(content["main"]["temp"])
        temp_min = float(content["main"]["temp_min"])
        temp_max = float(content["main"]["temp_max"])

        # si no tenemos datos de ese día creamos una nueva entrada en el diccionario
        if not days.get(day):
            days[day] = {"temp": [], "temp_min": [], "temp_max": []}
        # añadimos medición
        days[day]["temp"].append(temp)
        days[day]["temp_min"].append(temp_min)
        days[day]["temp_max"].append(temp_max)
        totals["temp"].append(temp)
        totals["temp_min"].append(temp_min)
        totals["temp_max"].append(temp_max)


def html_file(city, temp_data):
    """
    Abre para escritura el fichero donde guardaremos la salida html.
    :param city: Localidad de la que hacemos las mediciones.
    :param temp_data: JSON con las mediciones de OpenWeathers
    :return: manejador del fichero
    """
    # nombre fichero: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}
    # ejemplo: "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
    start_date = temp_data["list"][0]["dt_txt"]  # fecha primera medición
    end_date = temp_data["list"][-1]["dt_txt"]   # fecha última medición
    file_name = folder + city + "_" + start_date + "_" + end_date + ".html"
    # sustituimos en el nombre ":" por "." y " " por "-"
    file_name = file_name.replace(":", ".").replace(" ", "-")
    # abrimos fichero para escritura
    try:
        file = open(file_name, "wt")
    except IOError:
        print("No se puede crear el fichero html:", file_name)
        exit(3)
    return file


# Funciones para mostrar las temperaturas
def write_days_values(day, temps, file):
    """
    Escribirá la temperatura media, mínima y máxima del día que hemos pasado como parámetro y el número de
    mediciones.
    :param file: manejador de fichero donde se escribe el html. None si la salida es por pantalla.
    :param day: día en el que se han tomado los valores de la temperatura.
    :param temps: mediciones del día.
    :return salida_html: si es verdadero la salida es en un fichero
    """

    # cálculos y formateo del día
    day = f"{day[8:]}-{day[5:7]}-{day[0:4]}"  # formato dd-mm-aaaa
    temp_med = sum(temps['temp']) / len(temps['temp'])
    temp_min = min(temps['temp_min'])
    temp_max = max(temps['temp_max'])

    # muestro la información o en el fichero html o en pantalla
    if file:
        file.write(row_html(day, temp_med, temp_min, temp_max, len(temps['temp'])))
    else:
        print(f"Día {day}:\t"
              f"Temperatura media: {temp_med:.2f}º, "
              f"mínima: {temp_min}º y máxima: {temp_max}º. "
              f"Mediciones: {len(temps['temp'])}")


def write_totals_values(totals, file, data):
    """
    Escribirá la temperatura media, mínima y máxima global que hemos pasado como parámetro y el número de
    mediciones.
    :param data: número total de mediciones realizadas,
    :param totals: diccionario con los datos globales de las mediciones
    :param file: manejador de fichero donde se escribe el html. None si la salida es por pantalla.
    """

    # cálculos
    temp_med = sum(totals['temp']) / len(totals['temp'])
    temp_min = min(totals['temp_min'])
    temp_max = max(totals['temp_max'])
    if file:
        file.write(end_html(temp_med, temp_min, temp_max, data))
        file.close()
        print("Generado fichero", file.name, "con los datos.")
    else:
        print(f"\nTOTALES:\t\tTemperatura media: {temp_med:.2f}º, "
              f"mínima: {temp_min}º y máxima: {temp_max}º")


# Funciones para manejar el html
def begin_html(city):
    """
    :param city:
    :return: inicio del html del resumen del pronóstico del tiempo.
    """
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lectura de temperaturas en {city}</title>
</head>
<body>
    <center><p>Este programa nos muestra los resultados de las mediciones para los próximos 5 días en {city}</p>
        <table border="1">
            <tr>
                <th>Día</th>
                <th>Temperatura Media</th>
                <th>Temperatura Mínima</th>
                <th>Temperatura Máxima</th>
                <th>Nº Mediciones</th>
            </tr>"""


def row_html(day, temp_med, temp_min, temp_max, data):
    return f"""
            <tr>
                <td><center>{day}</center></td>
                <td><center>{temp_med:.2f}º</center></td>
                <td><center>{temp_min}º</center></td>
                <td><center>{temp_max}º</center></td>
                <td><center>{data}</center></td>
            </tr>"""


def end_html(temp_med, temp_min, temp_max, data):
    return f"""
            <tr>
                <th><center>TOTALES</center></th>
                <th><center>{temp_med:.2f}º</center></th>
                <th><center>{temp_min}º</center></th>
                <th><center>{temp_max}º</center></th>
                <th><center>{data}</center></th>
            </tr>
        </table>
    </center>
</body>
</html>
"""

# - PROGRAMA PRINCIPAL -
# Comprobamos si el número de parámetros es correcto
if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("La sintaxis es incorrecta.", file=sys.stderr)
    exit(1)

# Comprobamos si la salida es por pantalla o a un archivo html o hay que mostrar la ayuda
if len(sys.argv) == 3:
    is_html = True
    folder = sys.argv[2]
    if folder[-1] != "/" and folder[-1] != "\\":
        print("El nombre del directorio tiene que terminar en / ó en \\", file=sys.stderr)
        exit(3)
elif sys.argv[1] == "-h":
    show_help()
    exit(0)
else:
    is_html = False


city = sys.argv[1]    # localidad de la que vamos a hacer el pronóstico

# petición GET a OpenWeather
data = request_to_json(city)

# cálculos
days = dict()  # diccionario con clave el día y valor la lista de mediciones del día
totals = {"temp": [], "temp_min": [], "temp_max": []}  # lista de mediciones de todos los días
temp_calcs(days, totals, data)

# Resultados
# crear fichero html si es necesario
if is_html:
    file = html_file(city, data)
    file.write(begin_html(city))  # escribimos inicio html
else:
    file = None

# procesamos cada medición
for day, temps in days.items():
    write_days_values(day, temps, file)    # diario

# global
write_totals_values(totals, file, len(data["list"]))