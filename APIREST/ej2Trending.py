import requests
import os
"""
2. Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.

Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org

Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
"""
def trending_topic_movies(page, trendTime):
    #Construccion endpoint
    url = URL + TRENDING
    if trendTime == "S":
        url += WEEKLY
    else:
        url += DAILY

    p = {'api_key': os.getenv('MOVIEDB_ID'), 'language': "es", 'page' : str(page)}

    response = requests.get(url, params=p)
    if response.status_code == 200:
        return response.json()

def request_gender():
    while True:
        order_by_genders = input("¿Quieres organizarla en géneros? ( 'S' o 'N' ): ").upper()
        if order_by_genders in ["S", "N"]:
            break

    if order_by_genders != 'S':
        return 0
    else:
        GENDERSLIST = genders_of_movies()

        while True:
            show_genders(GENDERSLIST)
            try:
                gender = int(input("Introduce el código del género por el que quieres filtrar: "))
            except ValueError: # Si no introduce un entero
                gender = 0
            if gender in GENDERSLIST.keys():
                break
            print("ERROR: Código de género inválido")

    return gender

def genders_of_movies():
    url = URL + GENDERS
    p = {'api_key': os.getenv('MOVIEDB_ID'), 'language': "es"}
    response = requests.get(url, params=p)
    if response.status_code != 200:
        print("Error al hacer la petición:", response.url, "status:", response.status_code)
        exit(1)
    list_of_genders = response.json()
    genders = dict()
    for g in list_of_genders["genres"]:
        genders[g["id"]] = g["name"]

    return genders

def show_genders(GENDERSLIST):
    print("\nGÉNEROS")
    print()
    for code, gender in GENDERSLIST.items():
        print(f"{code}: {gender}")
    print()
    pass

def request_trend():
    while True:
        trendTime = input("¿Quieres ver el trending semanal o diario? ( 'S' o 'D' ): ").upper()
        if trendTime in ["S", "D"]:
            break
    return trendTime

## MAIN ##

# Datos
NUMMOVIES = 5
URL = "https://api.themoviedb.org/3"
WEEKLY = "/week"
DAILY = "/day"
TRENDING = "/trending/movie"
GENDERS = "/genre/movie/list"

print("Este programa te dará las películas trending según género.")

# Pido al usuario
trendTime = request_trend()

gender = request_gender()

numMovies = 0
page = 1

print("\nTRENDING TOPIC")
print()
while True:
    movies = trending_topic_movies(page, trendTime)
    for movie in movies['results']:
        if (gender == 0) or (gender in movie['genre_ids']): #Si ha pedido filtrar todas o coincide con las que ha pedido
            numMovies += 1
            print(f"{numMovies}: {movie['title']}")
            if numMovies == NUMMOVIES:  # Si ya ha encontrado cinco peliculas
                break
    page += 1
    if numMovies == NUMMOVIES: # Si ya ha encontrado cinco peliculas
        break