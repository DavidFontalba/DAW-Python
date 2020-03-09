import datetime

import requests
import os

"""
1. Usando esta API de OpenWeather que nos da el pronóstico del tiempo para una ciudad que se le pide al usuario de los
siguientes cinco días, mostrar:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.
Tened en cuenta que las respuestas de esta api referentes a los días y horas usan el tiempo en formato UNIX (UTC).
"""

def mediaArrayInt(vector):
    sumatorio = 0
    for i in range(len(vector)):
        sumatorio += vector[i]
    media = sumatorio / len(vector)
    return media

# Datos
url = "https://api.openweathermap.org/data/2.5/forecast"
print("Este programa te dará el pronóstico del tiempo de una ciudad para los próximos cinco días")
ciudad = input("Introduce una ciudad: ")
api_key = os.getenv('OPENWEATHER_ID')
p = {'q': ciudad, 'appid': api_key, 'units': 'metric'}

# Petición
r = requests.get(url, params=p)

tempMediaDia = []
tempMaxDia = []
tempMinDia = []

tempMediaGlobal = []
tempMaxGlobal = []
tempMinGlobal = []

if r.status_code == 200:
    contenido = r.json()
    diaActual = str(datetime.datetime.fromtimestamp(int(contenido['list'][0]['dt'])).strftime('%d'))

    for element in contenido['list']:
        # Me guardo el día por el que voy pasando
        diaAux = datetime.datetime.fromtimestamp(int(element['dt'])).strftime('%d')

        # Almaceno los valores en un array por cada uno para ir sacando los valores por dias
        tempMediaDia.append(element['main']['temp'])
        tempMaxDia.append(element['main']['temp_max'])
        tempMinDia.append(element['main']['temp_min'])

        # Cuando se cambie de día mostraré los resultados diarios
        if diaActual != diaAux:
            print("La temperatura media del día", diaActual, "es", mediaArrayInt(tempMediaDia), "º C")
            print("La temperatura máxima es", mediaArrayInt(tempMaxDia), "º C")
            print("La temperatura mínima es", mediaArrayInt(tempMinDia), "º C\n")

            tempMediaGlobal.append(mediaArrayInt(tempMediaDia))
            tempMaxGlobal.append(mediaArrayInt(tempMaxDia))
            tempMinGlobal.append(mediaArrayInt(tempMinDia))

            tempMediaDia = []
            tempMaxDia = []
            tempMinDia = []

            diaActual = diaAux

    # Cuando acabe el bucle y haya leído los cinco días, muestro los resultados globales
    print("La temperatura media de los cinco días es", mediaArrayInt(tempMediaGlobal), "º C")
    print("La temperatura máxima es", mediaArrayInt(tempMaxGlobal), "º C")
    print("La temperatura mínima es", mediaArrayInt(tempMinGlobal), "º C")
