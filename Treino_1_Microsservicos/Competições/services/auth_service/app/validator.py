import re

def validate_email(email):
    if not email:
        return False, "Email é obrigatorio"
    pattern= r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern,email):
        return False, "Email inválido"
    return True, ""

def validate_password(password):
    if not password:
        return False, "Senha é obrigatória"
    if len(password) <6:
        return 
    return True