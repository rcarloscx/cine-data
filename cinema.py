mport json
from math import fabs
from pickle import FALSE
import requests
import pandas as pd

#Urls de cinema 
fechasUrl="https://cinemas.com.ni/filter-fandango/fechas.json"
localesUrl="https://cinemas.com.ni/filter-fandango/Timestamp/locales.json"
peliculasUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$Timestamp/peliculas.json"
formatoUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$IdPelicula/formato.json"
horariosUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$Timestamp/$Formato/horarios.json"


def CinemaNi():
  fechas=requests.get(fechasUrl).json()["FECHAS"]
  cines=requests.get(localesUrl.replace('Timestamp', str(fechas[0]["Timestamp"]),1)).json()["LOCALES"]
  funcionesFinales=[]
  for cine in cines:
    pelicula=peliculasUrl.replace('$IdCine',cine['IdCinemas'],1)
    pelicula=pelicula.replace('$Timestamp',str(fechas[0]["Timestamp"]),1)
    pelicula=requests.get(pelicula).json()['PELICULAS']
    for peliculas in pelicula:
      dataCinema=[]
      dataCinema.append(cine['Nombre'])
      dataCinema.append(peliculas['NombrePelicula'])
      url= formatoUrl.replace("$IdCine",cine['IdCinemas'],1)
      url=url.replace('$IdPelicula',peliculas['IdPelicula'],1)
      urls=requests.get(url).json()['FORMATO']
      for uri in urls:
        dataCinema.append(uri['Label'])
        horarios= horariosUrl.replace("$IdCine",cine['IdCinemas'],1)
        horarios= horarios.replace("$Timestamp",str(fechas[0]["Timestamp"]),1)
        horarios= horarios.replace("$Formato",uri['IdPeliculaVista'],1)
        horario=requests.get(horarios).json()['HORARIOS']
        for funciones in horario:
          dataCinema.append(funciones['Hora'])
      funcionesFinales.append(dataCinema)
  return funcionesFinales
dfcinema= pd.DataFrame(CinemaNi())
dfcinema.to_excel("CinemaNi.xlsx", index=FALSE)
