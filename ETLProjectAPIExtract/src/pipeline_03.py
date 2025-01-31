import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import BitcoinPreco, Base
from dotenv import load_dotenv
import os


load_dotenv() #carregar as variáveis de ambiente do arquivo .env

POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')
POSTGRES_DB=os.getenv('POSTGRES_DB')

database_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

def criar_tabela():
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso")


def extract_dadosbitcoin():
    try:
        url = "https://api.coinbase.com/v2/prices/spot"
        response = requests.get(url)
        response.raise_for_status()  
        dados = response.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao extrair dados da API: {e}")
        return None

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

def salvar_dados_postgres(dados):
    try:
        session = Session()
        bitcoin_preco = BitcoinPreco(**dados)
        session.add(bitcoin_preco)
        session.commit()
        print("Dados salvos com sucesso no banco de dados")
    except Exception as e:
        print(f"Erro ao salvar dados no banco: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__": #defini o novo timesleep para 60 segundos para evitar sobrecarga na API e banimento do IP por excesso de requisições
    criar_tabela()  
    while True:
        try:
            dados = extract_dadosbitcoin()
            if dados:
                dados_transformados = transform_dadosbitcoin(dados)
                salvar_dados_postgres(dados_transformados)
            time.sleep(60)
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            time.sleep(60)
            continue