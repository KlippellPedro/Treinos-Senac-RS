from .database import get_connection
from mysql.connector import IntegrityError


# =========================
# LISTAR CONVIDADOS
# =========================
def list_guests(event_id=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM convidado"
    params = []

    if event_id:
        query += " WHERE id_evento=%s"
        params.append(event_id)

    cursor.execute(query, params)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result


# =========================
# BUSCAR POR ID
# =========================
def get_guest(guest_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM convidado WHERE id_convidado=%s",
        (guest_id,)
    )

    guest = cursor.fetchone()

    cursor.close()
    conn.close()
    return guest


# =========================
# CRIAR CONVIDADO (CPF ÚNICO)
# =========================
def create_guest(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
            INSERT INTO convidado 
            (id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, (
            data['id_evento'],
            data['nome'],
            data['sobrenome'],
            data['cpf'],
            data.get('telefone'),
            data.get('email'),
            data.get('numero_mesa'),
            data['tipo_convidado']
        ))

        conn.commit()
        return cursor.lastrowid

    except IntegrityError:
        conn.rollback()
        return None  # CPF duplicado

    finally:
        cursor.close()
        conn.close()


# =========================
# ATUALIZAR CONVIDADO
# =========================
def update_guest(guest_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        set_clause = ", ".join(f"{k}=%s" for k in data.keys())
        query = f"UPDATE convidado SET {set_clause} WHERE id_convidado=%s"

        cursor.execute(query, list(data.values()) + [guest_id])
        conn.commit()

        return True

    except IntegrityError:
        conn.rollback()
        return False

    finally:
        cursor.close()
        conn.close()


# =========================
# DELETAR CONVIDADO
# =========================
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


# =========================
# CHECK-IN (SERVIÇO SEPARADO E SEGURO)
# =========================
def checkin_guest(guest_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # 1. Evita check-in duplicado
        cursor.execute(
            "SELECT id_checkin FROM checkin WHERE id_convidado=%s",
            (guest_id,)
        )

        if cursor.fetchone():
            return False  # já fez check-in

        # 2. Registra check-in
        cursor.execute(
            "INSERT INTO checkin (id_convidado, id_usuario) VALUES (%s,%s)",
            (guest_id, user_id)
        )

        # 3. Atualiza status do convidado
        cursor.execute(
            "UPDATE convidado SET status='confirmado' WHERE id_convidado=%s",
            (guest_id,)
        )

        conn.commit()
        return True

    except IntegrityError:
        conn.rollback()
        return False

    finally:
        cursor.close()
        conn.close()