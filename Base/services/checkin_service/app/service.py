from .database import get_connection
import mysql.connector


def realizar_checkin(id_convidado, id_usuario):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
       
        cursor.execute("""
            SELECT id_convidado 
            FROM convidado 
            WHERE id_convidado = %s
        """, (id_convidado,))
        
        convidado = cursor.fetchone()

        if not convidado:
            return {"error": "Convidado não encontrado"}, 404

        cursor.execute("""
            INSERT INTO checkin (id_convidado, id_usuario)
            VALUES (%s, %s)
        """, (id_convidado, id_usuario))


        cursor.execute("""
            UPDATE convidado
            SET status = 'confirmado'
            WHERE id_convidado = %s
        """, (id_convidado,))

        return {"message": "Check-in realizado com sucesso"}, 201

    except mysql.connector.IntegrityError:

        return {"error": "Check-in já realizado"}, 400

    except Exception as e:
        return {"error": "Erro interno", "details": str(e)}, 500

    finally:
        cursor.close()
        conn.close()