import json
from math import fabs
import requests
import pandas as pd

# Cinepolis

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

#Urls de cinema 
fechasUrl="https://cinemas.com.ni/filter-fandango/fechas.json"
localesUrl="https://cinemas.com.ni/filter-fandango/Timestamp/locales.json"
peliculasUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$Timestamp/peliculas.json"
formatoUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$IdPelicula/formato.json"
horariosUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$Timestamp/$Formato/horarios.json"

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


#CINEMARK
cinemarksv={"Cinemark San Miguel":780, "Cinemark San Salvador":782,"Cinemark La Gran Vía":784}
cinemarkgt={"Cinemark Arkadia":2202,"Cinemark Majadas Once":2208, "Cinemark MetroCentro Villa Nueva":2206}
cinemarkhn={"Cinemark Megaplaza La Ceiba":2207,"Cinemark Citymall San Pedro Sula":774,"Galerias del Valle":2200,
"Cinemark Citymall Tegucigalpa":2201,"Cinemark Multiplaza Tegucigalpa":771}
cinemarkni={"Cinemark Metrocentro Managua":772}
cinemarkpa={"Cinemark Albrook Mall":795, "Cinemark Pacific Center":2209}
cinemarkcr={"Cinemark Citymall Alajuela":2204,"Cinemark Multiplaza Curridabat":773,
"Cinemark Multiplaza Escazú": 770, "Cinemark Oxigeno":2210}
def cinesCA(cinesSV):
    finalPeliculas=[]
    for idcine in cinesSV:
        uri='https://api.cinemarkca.com/api/vista/data/billboard?cinema_id='+str(cinesSV[idcine])
        data= requests.get(uri)
        datos=json.loads(data.content)
        for elements in datos[0]['movies']:

            for element2 in elements['movie_versions']:
                peliculas = []
                peliculas.append(idcine)
                peliculas.append(elements['title'])
                peliculas.append(elements['rating'])
                peliculas.append(elements['runtime'])
                peliculas.append(element2['title'])
                for element3 in element2['sessions']:
                    peliculas.append(element3['hour'])
                finalPeliculas.append(peliculas)

    return finalPeliculas

def CinemaNi():
  fechas=requests.get(fechasUrl).json()["FECHAS"]
  cines=requests.get(localesUrl.replace('Timestamp', str(fechas[0]["Timestamp"]),1)).json()["LOCALES"]
  funcionesFinales=[]
  for cine in cines:
    pelicula=peliculasUrl.replace('$IdCine',cine['IdCinemas'],1)
    pelicula=pelicula.replace('$Timestamp',str(fechas[0]["Timestamp"]),1)
    pelicula=requests.get(pelicula).json()['PELICULAS']
    for peliculas in pelicula:
      url= formatoUrl.replace("$IdCine",cine['IdCinemas'],1)
      url=url.replace('$IdPelicula',peliculas['IdPelicula'],1)
      urls=requests.get(url).json()['FORMATO']
      for uri in urls:
        dataCinema=[]
        dataCinema.append(cine['Nombre'])
        dataCinema.append(peliculas['NombrePelicula'])
        dataCinema.append('N/A')
        dataCinema.append('N/A')
        dataCinema.append(uri['Label'])
        horarios= horariosUrl.replace("$IdCine",cine['IdCinemas'],1)
        horarios= horarios.replace("$Timestamp",str(fechas[0]["Timestamp"]),1)
        horarios= horarios.replace("$Formato",uri['IdPeliculaVista'],1)
        #Hay peliculas que no tienen horarios, se puede validar con el tamanio de la lista "horario"
        horario=requests.get(horarios).json()['HORARIOS']
        for funciones in horario:
          dataCinema.append(funciones['Hora'])
        funcionesFinales.append(dataCinema)
  return funcionesFinales


carteleraSv = carteleraPorPais(urlSv, complejosSv)
carteleraSv.extend(cinesCA(cinemarksv))

carteleraGt = carteleraPorPais(urlGt, complejosGt)
carteleraGt.extend(cinesCA(cinemarkgt))

carteleraCr = carteleraPorPais(urlCr, complejosCr)
carteleraCr.extend(cinesCA(cinemarkcr))

carteleraHn = carteleraPorPais(urlHn, complejosHn)
carteleraHn.extend(cinesCA(cinemarkhn))

carteleraPa = carteleraPorPais(urlPa, complejosPa)
carteleraPa.extend(cinesCA(cinemarkpa))

carteleraNi = CinemaNi()
carteleraNi.extend(cinesCA(cinemarkni))

dfsv=pd.DataFrame(carteleraSv)
dfgt=pd.DataFrame(carteleraGt)
dfhn=pd.DataFrame(carteleraHn)
dfni=pd.DataFrame(carteleraNi)
dfcr=pd.DataFrame(carteleraCr)
dfpa=pd.DataFrame(carteleraPa)

dfsv.to_excel("CineDataSv.xlsx", index=False)
dfgt.to_excel("CineDataGt.xlsx", index=False)
dfhn.to_excel("CineDatahn.xlsx" ,index=False)
dfni.to_excel("CineDatani.xlsx" ,index=False)
dfcr.to_excel("CineDatacr.xlsx", index=False)
dfpa.to_excel("CineDatapa.xlsx", index=False)
print(dfsv)
