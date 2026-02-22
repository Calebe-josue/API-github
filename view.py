from controller import*
from time import sleep

nome = str(input('Digite seu nome de usuário do github para ter acesso a seus eventos\n'))

pes1 = Eventos(nome)
acessando = pes1.acessar_api()

if not acessando:
    print('Erro, usuário não encontrado')
else:
    arquivo = abrir_arquivo('dados.json')

    for i in arquivo:
        sleep(1)
        print(f'você teve um {i["type"]} no repositório {i["repo"]["url"]}')