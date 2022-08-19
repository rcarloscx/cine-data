import requests
import json

url = 'https://www.cinepolis.com.sv/manejadores/CiudadesComplejos.ashx'
url2 = 'https://www.cinepolis.com.sv/Cartelera.aspx/GetNowPlayingByCity'
response = requests.get(url)

datos = response.json()
