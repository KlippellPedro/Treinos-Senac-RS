from .database import get_connection
from mysql.connector import InternalError

def list_guest():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM convidado")
    data=cursor.fetchall()

    cursor.close()
    conn.close()
    return data

def get_guest(guest_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM convidado WHERE id_convidado=%s", (guest_id,))
    data=cursor.fetchone()

    cursor.close()
    conn.close()
    return data

def create_guest(data):
    conn=get_connection()
    cursor=conn.cursor()

    query= """INSERT INTO convidado (nome,email,cpf,telefone,tipo,status,id_evento) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query,(
        data["nome"],
        data["email"],
        data["cpf"],
        data["telefone"],
        data["tipo"],
        data["status"],
        data["id_evento"]
    ))
    conn.commit()
    cursor.close()
    conn.close()

def update_guest(guest_id,data):
    conn=get_connection()
    cursor=conn.cursor()
    query="""UPDATE convidado SET nome=%s,email=%s,cpf=%s,telefone=%s,tipo=%s,status=%s,id_evento=%s WHERE id_convidado=%s"""
    cursor.execute(query,(
        data["nome"],
        data["email"],
        data["cpf"],
        data["telefone"],
        data["tipo"],
        data["status"],
        data["id_evento"],
        guest_id
    ))
    conn.commit()
    cursor.close()
    conn.close()

def delete_guest(guest_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM convidado WHERE id_convidado=%s",(guest_id,))

    conn.commit()
    cursor.close()
    conn.close()