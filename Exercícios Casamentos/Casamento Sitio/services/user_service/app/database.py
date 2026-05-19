import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("localhost"),
            user=os.getenv("root"),
            password=os.getenv(""),
            database=os.getenv("casamento_sitio"),
            autocommit=True
        )
        return conn
    except Error as e:
        print(f"[ERRO DB] {e}")
        return None