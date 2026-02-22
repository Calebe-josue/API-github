import json
from controller import*

def salvar_arquivo(nome,api):
    with open(nome,'w') as arq:
        json.dump(arq,api,indent=4)

