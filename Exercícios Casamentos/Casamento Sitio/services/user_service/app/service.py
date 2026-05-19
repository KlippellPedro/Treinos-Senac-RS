from .database import get_connection
from .validators import hash_password, check_password, validate_email, validate_password, validate_cpf
from mysql.connector import IntegrityError


def list_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_usuario, nome, cpf, email, perfil FROM usuario")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_usuario, nome, cpf, email, perfil FROM usuario WHERE id_usuario=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def create_user(data):
    email_valid, msg = validate_email(data.get("email"))
    if not email_valid:
        return None, msg
    password_valid, msg = validate_password(data.get("senha"))
    if not password_valid:
        return None, msg
    cpf_valid, msg = validate_cpf(data.get("cpf"))
    if not cpf_valid:
        return None, msg

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuario (nome, cpf, email, senha, perfil) VALUES (%s,%s,%s,%s,%s)",
            (data['nome'], data['cpf'], data['email'], hash_password(data['senha']), data['perfil'])
        )
        conn.commit()
        user_id = cursor.lastrowid
    except IntegrityError as e:
        conn.rollback()
        cursor.close()
        conn.close()
        return None, "Email ou CPF já cadastrado"
    cursor.close()
    conn.close()
    return user_id, None

def update_user(user_id, data):
    conn = get_connection()
    cursor = conn.cursor()
    set_clause = []
    values = []

    for key in ["nome", "cpf", "email", "senha", "perfil"]:
        if key in data:
            if key == "senha":
                values.append(hash_password(data[key]))
            else:
                values.append(data[key])
            set_clause.append(f"{key}=%s")

    query = f"UPDATE usuario SET {', '.join(set_clause)} WHERE id_usuario=%s"
    cursor.execute(query, values + [user_id])
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id_usuario=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()