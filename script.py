import json
from math import fabs
import requests
import pandas as pd

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
            peliculas = []
            peliculas.append(idcine)
            peliculas.append(elements['title'])
            peliculas.append(elements['rating'])
            peliculas.append(elements['runtime'])
            for element2 in elements['movie_versions']:
                peliculas.append(element2['title'])
                for element3 in element2['sessions']:
                    peliculas.append(element3['hour'])
            finalPeliculas.append(peliculas)

    return finalPeliculas

dfsv= pd.DataFrame(cinesCA(cinemarksv))
dfgt=pd.DataFrame(cinesCA(cinemarkgt))
dfhn=pd.DataFrame(cinesCA(cinemarkhn))
dfni=pd.DataFrame(cinesCA(cinemarkni))
dfcr=pd.DataFrame(cinesCA(cinemarkcr))
dfpa=pd.DataFrame(cinesCA(cinemarkpa))

dfsv.to_excel("CinemarkDataSv.xlsx", index=False)
dfgt.to_excel("CinemarkDataGt.xlsx", index=False)
dfhn.to_excel("CinemarkDatahn.xlsx" ,index=False)
dfni.to_excel("CinemarkDatani.xlsx" ,index=False)
dfcr.to_excel("CinemarkDatacr.xlsx", index=False)
dfpa.to_excel("CinemarkDatapa.xlsx", index=False)
print(dfsv)
