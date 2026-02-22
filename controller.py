import requests
from model import*

class Eventos:
    def __init__(self,nome):
        self.nome = nome

    def acessar_api(self):
        url = 'https://api.github.com/users/'+self.nome+'/events'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            salvar_arquivo('dados.json',data)
            return True
        elif response.status_code == 404:
            return False
