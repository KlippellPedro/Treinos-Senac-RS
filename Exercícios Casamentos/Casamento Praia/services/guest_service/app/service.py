from .database import get_connection
from mysql.connector import IntegrityError

def list_guest(event_id=None):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query= "SELECT * FROM convidado"