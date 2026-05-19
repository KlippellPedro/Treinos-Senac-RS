from database import get_connection
from validators import hash_password

def list_user():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_user(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id_usuario=%s", (user_id,))
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def create_user(data):
    conn=get_connection()
    cursor=conn.cursor()
    query="""INSERT INTO usuario (nome,cpf,email,senha,perfil) VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(query,(data["nome"], data["cpf"], data["email"], hash_password(data["senha"]), data["perfil"]))
    data=cursor.fetchall
    conn.commit()
    cursor.close()
    conn.close()

def update_user(data,user_id):
    conn=get_connection()
    cursor=conn.cursor()
    query="""UPDATE usuario SET (nome=%s,cpf=%s,email=%s,senha=%s,perfil=%s) WHERE id_usuario=%s"""
    cursor.execute(query,(data["nome"], data["cpf"],data["email"],data["perfil"], user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE * FROM usuario WHERE id_usuario=%s", (user_id))
    conn.commit()
    cursor.close()
    conn.close()