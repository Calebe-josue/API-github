from controller import*
from time import sleep

nome = str(input('Digite seu nome de usuário do github para ter acesso a seus eventos\n'))

pes1 = Eventos(nome)
pes1.acessar_api()

arquivo = abrir_arquivo('dados.json')

for i in arquivo:
    sleep(1)
    print(f'você teve um {i["type"]} no repositório {i["repo"]["url"]}')