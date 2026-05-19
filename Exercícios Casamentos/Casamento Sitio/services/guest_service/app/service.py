from .database import get_connection
from mysql.connector import IndentationError

def list_guests(event_id=None):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="SELECT * FROM convidado"
    params=[]
    if event_id:
        query+="WHERE id_usuario=%s"
        params.append(event_id)
    cursor.execute(query,params)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_guest(guest_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT *FROM convidado WHERE id_convidadp=%s", (guest_id))
    guest=cursor.fetchall()
    cursor.close()
    conn.close()
    return guest

def create_guest(data):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query= """INSERT INTO convidado (id_evento,nome,categoria) VALUES (%s,%s,%s)"""
    cursor.execute(query, (data['id_evento'], data['nome'], data['categoria']))
    conn.commit()
    guest_id=cursor.lastrowid
    cursor.close()
    conn.close()
    return guest_id

def update_guest(guest_id, data):
    conn=get_connection()
    cursor=conn.cursor()
    set_clause=", ".join(f"{k}=%s" for k in data.keys())
    query= f"UPDATE convidados SET {set_clause} WHERE id_convidado"
    cursor.execute(query, list(data.values()) + {guest_id})
    conn.commit()
    cursor.close()
    conn.close()

def delete_guest(guest_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM convidados WHERE id_convidado=%s", (guest_id))
    conn.commit()
    cursor.close()
    conn.close()

def checkin_guest(guest_id,user_id):
    conn=get_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO checkin (id_convidado, id_usuario) VALUES (%s,%s)", (guest_id,user_id))
        cursor.execute("UPDATE convidado SET status='confirmado' WHERE id_convidado=%s", (guest_id))
        conn.commit()
        return True
    except InterruptedError:
        return False
    finally:
        cursor.close()
        conn.close()