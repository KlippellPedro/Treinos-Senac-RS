from .database import get_connection
from mysql.connector import IntegrityError


def list_guests():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM convidado")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_guest(guest_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM convidado WHERE id_convidado=%s",
        (guest_id,)
    )
    data = cursor.fetchone()

    cursor.close()
    conn.close()
    return data


def create_guest(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
            INSERT INTO convidado 
            (id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            data["id_evento"],
            data["nome"],
            data["sobrenome"],
            data["cpf"],
            data["telefone"],
            data["email"],
            data["numero_mesa"],
            data["tipo_convidado"]
        ))

        conn.commit()
        return cursor.lastrowid

    except IntegrityError as e:
        # CPF duplicado ou outro erro de chave única
        if "cpf" in str(e):
            return {"error": "CPF já cadastrado"}

        return {"error": "Erro de integridade no banco"}

    finally:
        cursor.close()
        conn.close()



def update_guest(guest_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE convidado
        SET nome=%s,
            sobrenome=%s,
            cpf=%s,
            telefone=%s,
            email=%s,
            numero_mesa=%s,
            tipo_convidado=%s
        WHERE id_convidado=%s
    """

    cursor.execute(query, (
        data["nome"],
        data["sobrenome"],
        data["cpf"],
        data["telefone"],
        data["email"],
        data["numero_mesa"],
        data["tipo_convidado"],
        guest_id
    ))

    conn.commit()
    cursor.close()
    conn.close()



def delete_guest(guest_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM convidado WHERE id_convidado=%s",
        (guest_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()