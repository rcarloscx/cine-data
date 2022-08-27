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
CinemarkSV=[
    {"id":780,"nombre":"Metrocentro San Miguel","Ciudad":"San Miguel"} ,
    {"id":782,"nombre":"Metrocentro San Salvador", "Ciudad":"San Salvador"},
    {"id":784,"nombre":"La Gran Vía", "Ciudad":"San Salvador"}
]
CinemarkGT=[
    {"id":2202,"nombre":"Arkadia","Ciudad":"Guatemala"},
    {"id":2208,"nombre":"Majadas Once","Ciudad":"Guatemala"}, 
    {"id":2206,"nombre":"MetroCentro Villa Nueva","Ciudad":"Villa Nueva"}
]
CinemarkHN=[
    {"id":2207,"nombre":"Megaplaza La Ceiba", "Ciudad":"La Ceiba"},
    {"id":774,"nombre":"Citymall San Pedro Sula", "Ciudad":"San Pedro Sula"},
    {"id":2200,"nombre":"Galerias del Valle","Ciudad":"San Pedro Sula"},
    {"id":2201,"nombre":"Citymall Tegucigalpa","Ciudad":"Tegucigalpa"},
    {"id":771,"nombre":"Multiplaza Tegucigalpa", "Ciudad":"Tegucigalpa"}
]
CinemarkNI=[
    {"id":772,"nombre":"Metrocentro Managua","Ciudad":"Managua"}
]
CinemarkPA=[
    {"nombre":"Albrook Mall","id":795,"Ciudad":"Panama"},
    {"nombre":"Pacific Center","id":2209,"Ciudad":"Panama"}
]
CinemarkCR=[
    {"id":2204,"nombre":"Citymall Alajuela","Ciudad":"Alajuela"},
    {"id":773,"nombre":"Multiplaza Curridabat","Ciudad":"Curridabat"},
    {"id": 770,"nombre":"Multiplaza Escazú","Ciudad":"Escazú"}, 
    {"id":2210,"nombre":"Oxigeno","Ciudad":"Heredia"}
]

#Diccionario Cinemas
cinemas=[
  {"IdCinemas":"CNM01", "Nombre":"Galerias","Ciudad":"Managua"},
  {"IdCinemas":"CNM02", "Nombre":"PLAZA INTER","Ciudad":"Managua"},
  {"IdCinemas":"CNM03","Nombre":"BELLO HORIZONTE", "Ciudad":"Managua"},
  {"IdCinemas":"CNM05","Nombre":"MASAYA","Ciudad":"Masaya"}
  ]

def cinesCA(cinesSV):
    finalPeliculas=[]
    for idcine in cinesSV:
        uri='https://api.cinemarkca.com/api/vista/data/billboard?cinema_id='+str(idcine['id'])
        data= requests.get(uri)
        datos=json.loads(data.content)
        for elements in datos[0]['movies']:

            for element2 in elements['movie_versions']:
                peliculas = []
                peliculas.append(idcine['nombre'])
                peliculas.append(elements['title'])
                peliculas.append(idcine['Ciudad'])
                peliculas.append('Cinemark')
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
  for cine in cinemas:
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
        dataCinema.append(cine['Ciudad'])
        dataCinema.append("Cinemas")
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
carteleraSv.extend(cinesCA(CinemarkSV))

carteleraGt = carteleraPorPais(urlGt, complejosGt)
carteleraGt.extend(cinesCA(CinemarkGT))

carteleraCr = carteleraPorPais(urlCr, complejosCr)
carteleraCr.extend(cinesCA(CinemarkCR))

carteleraHn = carteleraPorPais(urlHn, complejosHn)
carteleraHn.extend(cinesCA(CinemarkHN))

carteleraPa = carteleraPorPais(urlPa, complejosPa)
carteleraPa.extend(cinesCA(CinemarkPA))

carteleraNi = CinemaNi()
carteleraNi.extend(cinesCA(CinemarkNI))

dfsv=pd.DataFrame(carteleraSv)
dfgt=pd.DataFrame(carteleraGt)
dfhn=pd.DataFrame(carteleraHn)
dfni=pd.DataFrame(carteleraNi)
dfcr=pd.DataFrame(carteleraCr)
dfpa=pd.DataFrame(carteleraPa)

dfsv.to_excel("data/our/El Salvador.xlsx", index=False)
dfgt.to_excel("data/our/Guatemala.xlsx", index=False)
dfhn.to_excel("data/our/Honduras.xlsx" ,index=False)
dfni.to_excel("data/our/Nicaragua.xlsx" ,index=False)
dfcr.to_excel("data/our/Costa Rica.xlsx", index=False)
dfpa.to_excel("data/our/Panama.xlsx", index=False)
print(dfsv)
