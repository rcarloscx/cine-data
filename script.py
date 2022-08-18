import json
import requests
import pandas as pd

#CINEMARK

uri='https://api.cinemarkca.com/api/vista/data/billboard?cinema_id=780'
data= requests.get(uri)
datos=json.loads(data.content)
finalPeliculas=[]
for elements in datos[0]['movies']:
    peliculas = []
    peliculas.append(elements['title'])
    peliculas.append(elements['rating'])
    peliculas.append(elements['runtime'])
    for element2 in elements['movie_versions']:
        peliculas.append(element2['title'])
        for element3 in element2['sessions']:
            peliculas.append(element3['hour'])
    finalPeliculas.append(peliculas)

df = pd.DataFrame(finalPeliculas)
print(df)
df.to_csv("cinemark1.csv")
