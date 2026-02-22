import json

def salvar_arquivo(nome,json):
    with open(nome,'w',encoding='utf-8') as arq:
        json.dump(json,arq,indent=4)

