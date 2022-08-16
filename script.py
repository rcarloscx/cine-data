import requests

res = requests.get('https://www.cinepolis.com.sv/manejadores/CiudadesComplejos.ashx')

print(res.json())
