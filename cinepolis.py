import requests
import json

url = 'https://www.cinepolis.com.sv/manejadores/CiudadesComplejos.ashx'
url2 = 'https://www.cinepolis.com.sv/Cartelera.aspx/GetNowPlayingByCity'
response = requests.get(url)

datos = response.json()
for ciudad in datos:
    #print(ciudad['Clave'])
    body = {'claveCiudad':''+ciudad['Clave'], 'esVIP': 'false'}
    #print(body)
    jsonPeliculas = requests.post(url2, json = body).json()['d']
    cinesPorCiudad = jsonPeliculas['Cinemas']
    for cineCiudad in cinesPorCiudad:
        peliculas = cineCiudad['Dates'][0]['Movies']
        for pelicula in peliculas:
            for formato in pelicula['Formats']:
                peli = []
                #Aqui se imprime el nombre del cine
                peli.append(cineCiudad['Name'])
                peli.append(pelicula['Title'])
                peli.append(pelicula['Rating'])
                peli.append(pelicula['RunTime'])
                #pelis.append(peli)
                peli.append(''+pelicula['Title']+' ('+formato['Name']+')')
                pelis.append(peli)
                for showtime in formato['Showtimes']:
                    peli.append(showtime['Time'])


for peli in pelis:
    print(peli)

