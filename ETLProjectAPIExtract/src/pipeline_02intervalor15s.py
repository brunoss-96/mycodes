import time
import requests
from tinydb import TinyDB
import os
from datetime import datetime

def extract_dadosbitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return(dados)

def transform_dadosbitcoin(dados):
    valor = dados['data']['amount']
    criptomoeda = dados['data']['base']
    moeda = dados['data']['currency'] 

    dados_transformados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda
    }
    return dados_transformados

def salvar_dados_tinydb(dados, pasta_base='ETLProjectAPIExtract', db_name='dadosbitcoin_{}.json'):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  #essas duas linhas são para criar um nome único para o arquivo com data e hora de cada cotacao
    db_name = db_name.format(timestamp)    
    os.makedirs(pasta_base, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_base, db_name)
    db = TinyDB(caminho_arquivo)
    db.insert(dados)
    print(f"Dados salvos com sucesso no banco de dados {caminho_arquivo}")


if __name__ == "__main__":
    while True:
        dados = extract_dadosbitcoin()
        dados_transformados = transform_dadosbitcoin(dados)
        salvar_dados_tinydb(dados_transformados)
        time.sleep(15)