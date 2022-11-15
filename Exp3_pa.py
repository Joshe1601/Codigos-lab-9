import requests
from datetime import datetime

data_urls = ["http://157.245.83.163/mes2",
            "http://157.245.83.163/mes3",
            "http://157.245.83.163/mes4",
            "http://157.245.83.163/mes5"]

def descargar(url):
    r = requests.get(url, allow_redirects=True)
    open(f'{url[-4:]}.csv', 'wb').write(r.content)
    print(f"Descarga de {url[-4:]} realizada")

inicio = datetime.now()
for url in data_urls:
    descargar(url)

final = datetime.now()

print(f"Tiempo de ejecucion: {final-inicio}")