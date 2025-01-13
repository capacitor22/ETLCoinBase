import requests
import time
import os
""" import logging
import logfire
from logging import basicConfig, getLogger """
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, BitcoinPreco

#Configuracao LogFire
""" logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy() """

# Variaveis de ambiente
load_dotenv()
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
POSTGRES_DB=os.getenv("POSTGRES_DB")

# Database URL
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def criar_tabela():
    """Cria a tabela no DB se existir"""
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso!")


def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados

def transform_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().timestamp()
    timestamp = datetime.now()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }

    return dados_transformados


def salvar_dados_postgres(dados):
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")


if __name__ == "__main__":
    criar_tabela()
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")
    #Extração dos dados
    while True:
        dados_json = extract_dados_bitcoin()
        dados_tratados = transform_dados_bitcoin(dados_json)
        salvar_dados_postgres(dados_tratados)
        time.sleep(15)

