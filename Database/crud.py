# Serve para biaxar o arquivo mysql connector e conectar com o banco
# C:/Users/PEDRONADALONKLIPPEL/AppData/Local/Programs/Python/Python314/python.exe -m pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def abrir_conexao():
    """Cria e retorna a conexão com o banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='nome do banco'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

def criar_tabela():
    """Garante que a tabela exista antes de qualquer operação."""
    db = abrir_conexao()
    if db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        """)
        db.close()

# --- OPERAÇÕES DO CRUD ---

def inserir_usuario(nome, email):
    """CREATE: Insere um novo registro."""
    db = abrir_conexao()
    if db:
        cursor = db.cursor()
        sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
        cursor.execute(sql, (nome, email))
        db.commit()
        print(f"Usuário {nome} inserido com sucesso!")
        db.close()

def listar_usuarios():
    """READ: Retorna todos os registros."""
    db = abrir_conexao()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        db.close()
        return usuarios
    return []

def atualizar_email(id_usuario, novo_email):
    """UPDATE: Atualiza o email de um usuário pelo ID."""
    db = abrir_conexao()
    if db:
        cursor = db.cursor()
        sql = "UPDATE usuarios SET email = %s WHERE id = %s"
        cursor.execute(sql, (novo_email, id_usuario))
        db.commit()
        print(f"ID {id_usuario} atualizado para: {novo_email}")
        db.close()

def deletar_usuario(id_usuario):
    """DELETE: Remove um registro pelo ID."""
    db = abrir_conexao()
    if db:
        cursor = db.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (id_usuario,))
        db.commit()
        print(f"Usuário ID {id_usuario} removido.")
        db.close()

if __name__ == "__main__":
    criar_tabela()
    inserir_usuario("Ana Silva", "ana@email.com")
    inserir_usuario("Carlos Souza", "carlos@email.com")
    print("\nLista Atual:")
    for u in listar_usuarios():
        print(u)
    atualizar_email(1, "ana.nova@provedor.com")
    deletar_usuario(2) # O numero "2" é o ID 
    print("\nResultado Final:")
    print(listar_usuarios())