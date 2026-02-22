import requests
from model import*

url = 'https://api.github.com/users/Calebe-josue/events'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    salvar_arquivo('dados.json',data)