import requests


URL = 'https://randomuser.me/api/'

numero_de_nombres = int(input('Cuántos nombres de usuarios necesitas?: '))
respuesta = requests.get(URL, params={'results': numero_de_nombres})


if respuesta.status_code == 200:
    carga = respuesta.json()
    resultado = carga.get('results')

    for i in resultado:
        nombre = i.get('name')

        print(f"{nombre['title']} {nombre['first']} {nombre['last']}")