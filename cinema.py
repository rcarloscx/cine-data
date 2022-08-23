import json
from math import fabs
import requests
import pandas as pd

#Urls de cinema 
fechasUrl="https://cinemas.com.ni/filter-fandango/fechas.json"
localesUrl="https://cinemas.com.ni/filter-fandango/Timestamp/locales.json"
peliculasUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$Timestamp/peliculas.json"
formatoUrl="https://cinemas.com.ni/filter-fandango/$idCine/$IdPelicula/formato.json"
horariosUrl="https://cinemas.com.ni/filter-fandango/$IdCine/$Timestamp/$Formato/horarios.json"

#Iterar fechas

fechas=requests.get(fechasUrl).json()["FECHAS"]
for date in fechas:
  #Locales
  locales=localesUrl.replace('Timestamp', str(date["Timestamp"]),1)
  cines=requests.get(locales).json()["LOCALES"]

  print(cines)
  #Comentario
  
  break
    

