import mysql.connector
from mysql.connector import Error

# Acesso a variáveis de ambiente
import os
from dotenv import load_dotenv

# Carrega variáveis definidas no arquivo .env
load_dotenv()


def get_connection():
    """
    Cria e retorna uma conexão com o banco de dados MySQL.

    Usa variáveis de ambiente para:
    - host
    - usuário
    - senha
    - nome do banco

    Configura autocommit=True para operações imediatas.

    Em caso de falha, imprime erro e retorna None.
    """

    try:
        # Cria a conexão com MySQL usando dados do .env
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),       # host do banco
            user=os.getenv("DB_USER"),       # usuário
            password=os.getenv("DB_PASS"),   # senha
            database=os.getenv("DB_NAME"),   # nome do banco
            autocommit=True                  # commit automático
        )

        # Retorna o objeto de conexão
        return conn

    except Error as e:
        # Loga o erro no console e retorna None
        print(f"[ERRO DB] {e}")
        return None