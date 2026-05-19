import re

def validator_email(email):
    if not email:
        return False, "Email é obrigatorio"
    pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern,email):
        return False, "email invalido"
    return True, ""

def validate_password(password):
    if not password:
        return False,"Senha é obrigatorio"
    if len(password)<6:
        return False, "Senha precisa ter mais que 6 caracteres"
    return True, ""
