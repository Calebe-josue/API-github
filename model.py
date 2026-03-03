import json
# model para manipular aquivo json

def salvar_arquivo(nome,api): # Cria um novo arquivo a cada requisição de um usuário
    with open(nome,'w',encoding='utf-8') as arq:
        json.dump(api,arq,indent=4)


def abrir_arquivo(nome): # Abre o arquivo para obter os dados (eventos)
    with open(nome,'r',encoding='utf-8') as arq:
        return json.load(arq)
