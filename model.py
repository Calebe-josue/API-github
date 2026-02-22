import json

def salvar_arquivo(nome,api):
    with open(nome,'w',encoding='utf-8') as arq:
        json.dump(api,arq,indent=4)


def abrir_arquivo(nome):
    with open(nome,'r',encoding='utf-8') as arq:
        return json.load(arq)
