import re

def validate_email(email):
    if not email:
        return False, "Email é obrigatório"
    pattern= r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern,email):
        return False,"Email inválido"
    return True, None

def validate_password(password):
    if not password:
        return False, "Senha é obrigatório"
    if len(password) <6:
        return False, "Senha deve ter ao menos 6 caracteres"
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        return False, "Senha deve conter letras e números"
    return True, None
