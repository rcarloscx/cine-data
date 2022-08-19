import requests
import json
import pandas as pd

complejosSv = 'https://www.cinepolis.com.sv/manejadores/CiudadesComplejos.ashx'
complejosGt = 'https://www.cinepolis.com.gt/manejadores/CiudadesComplejos.ashx'
complejosCr = 'https://www.cinepolis.co.cr/manejadores/CiudadesComplejos.ashx'
complejosHn = 'https://www.cinepolis.com.hn/manejadores/CiudadesComplejos.ashx'
complejosPa = 'https://www.cinepolis.com.pa/manejadores/CiudadesComplejos.ashx'

urlSv = 'https://www.cinepolis.com.sv/Cartelera.aspx/GetNowPlayingByCity'
urlGt = 'https://www.cinepolis.com.gt/Cartelera.aspx/GetNowPlayingByCity'
urlCr = 'https://www.cinepolis.co.cr/Cartelera.aspx/GetNowPlayingByCity'
urlHn = 'https://www.cinepolis.com.hn/Cartelera.aspx/GetNowPlayingByCity'
urlPa = 'https://www.cinepolis.com.pa/Cartelera.aspx/GetNowPlayingByCity'


def carteleraPorPais(urlCine, complejos):
    pelis = []
    response = requests.get(complejos)
    data = response.json()
    for ciudad in data:
        #Body para hacer post de la ciudad
        body = {'claveCiudad':''+ciudad['Clave'], 'esVIP': 'false'}
        jsonPeliculas = requests.post(urlCine, json = body).json()['d']
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
    return pelis
#Cartelera El Salvador
carteleraSv = carteleraPorPais(urlSv, complejosSv)
dfsv=pd.DataFrame(carteleraSv)
dfsv.to_excel("CinepolisDataSv.xlsx", index=False)

#Cartelera Guatemala
carteleraGt = carteleraPorPais(urlGt, complejosGt)
dfgt=pd.DataFrame(carteleraGt)
dfgt.to_excel("CinepolisDataGt.xlsx", index=False)

#Cartelera Costa Rica
carteleraCr = carteleraPorPais(urlCr, complejosCr)
dfcr=pd.DataFrame(carteleraCr)
dfcr.to_excel("CinepolisDataCr.xlsx", index=False)

#Cartelera Honduras
carteleraHn = carteleraPorPais(urlHn, complejosHn)
dfhn=pd.DataFrame(carteleraHn)
dfhn.to_excel("CinepolisDataHn.xlsx", index=False)

#Cartelera Panama
carteleraPa = carteleraPorPais(urlPa, complejosPa)
dfpa=pd.DataFrame(carteleraPa)
dfpa.to_excel("CinepolisDataPa.xlsx", index=False)


