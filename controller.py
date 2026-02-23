import requests
from model import*
# Controlador que consome a API e salva em um json

class Eventos:
    """Essa classe acessa a API do github pelo nome de usuário, acessando todos seus eventos."""
    def __init__(self,nome):
        self.nome = nome

    def acessar_api(self): # Acessa o endpoint com o nome de usuário fornecido.
        url = 'https://api.github.com/users/'+self.nome+'/events' #Url do endpoint da API que pega os eventos
        response = requests.get(url)
        if response.status_code == 200: #Verifica se o nome de usuário está correto pelo status code
            data = response.json()
            salvar_arquivo('dados.json',data)
            return True
        elif response.status_code == 404: # Retorna valor False caso receba um 404 - Not Found, que significa usuário não encontrado.
            return False
