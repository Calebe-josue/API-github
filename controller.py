import requests
from model import*

url = 'https://api.github.com/users/calebe-josue/events'

resposta = requests.get(url)
data = resposta.json()

salvar_arquivo('dados.json',data)
