import mysql.connector  # Importa o conector MySQL 
from mysql.connector import Error  # Importa a classe de erro para tratar exceções do MySQL
import os  # Permite acessar variáveis de ambiente do sistema
from dotenv import load_dotenv  # Permite carregar variáveis do arquivo .env

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Função responsável por criar e retornar uma conexão com o banco de dados
def get_connection():
    try:
        # Lê as variáveis de ambiente necessárias para conexão com o banco
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        database = os.getenv("DB_NAME")

        # Verifica se as variáveis essenciais estão configuradas
        if not all([host, user, database]):
            raise Exception("Variáveis de ambiente não configuradas")

        # Cria a conexão com o banco MySQL usando os dados fornecidos
        conn = mysql.connector.connect(
            host=host,        # Endereço do servidor do banco 
            user=user,        # Usuário do banco
            password=password,  # Senha do banco
            database=database,  # Nome do banco de dados
            autocommit=True   # Ativa commit automático para operações INSERT, UPDATE, DELETE
        )

        # Retorna a conexão ativa
        return conn

    except Error as e:
        # Caso ocorra erro na conexão, imprime no console
        print(f"[ERRO DB] {e}")
        
        # Retorna None para indicar falha na conexão
        return None