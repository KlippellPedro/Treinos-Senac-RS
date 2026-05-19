import re  # Importa o módulo de expressões regulares, necessário para validar padrões de texto email e senha.

# Função para validar o email
def validate_email(email):
    if not email:
        # Se nenhum email foi fornecido, retorna False e a mensagem de erro
        return False, "Email é obrigatório"

    # Define o padrão de email usando expressão regular
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Verifica se o email fornecido corresponde ao padrão
    if not re.match(pattern, email):
        # Se não corresponder, retorna False e a mensagem de erro
        return False, "Email inválido"

    # Se passar todas as verificações, retorna True e None (nenhum erro)
    return True, None


# Função para validar a senha
def validate_password(password):
    if not password:
        # Se nenhuma senha foi fornecida, retorna False e a mensagem de erro
        return False, "Senha é obrigatória"

    if len(password) < 6:
        # Se a senha tiver menos de 6 caracteres, retorna False e a mensagem de erro
        return False, "Senha deve ter ao menos 6 caracteres"

    # Verifica se a senha contém pelo menos uma letra e um número
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        # Se faltar letra ou número, retorna False e a mensagem de erro
        return False, "Senha deve conter letras e números"

    # Se passar todas as verificações, retorna True e None (nenhum erro)
    return True, None



class Validator:
    @staticmethod
    def validate_email(email):
        """
        Valida se o email fornecido é válido.

        Parâmetros:
        email (str): O endereço de email a ser validado.

        Retorna:
        tuple: (bool, str ou None)
            - True, None se o email for válido
            - False, mensagem de erro se o email for inválido ou ausente
        """
        # Se nenhum email foi fornecido, retorna False e a mensagem de erro
        if not email:
            return False, "Email é obrigatório"

        # Define o padrão de email usando expressão regular
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        # Verifica se o email fornecido corresponde ao padrão
        if not re.match(pattern, email):
            # Se não corresponder, retorna False e a mensagem de erro
            return False, "Email inválido"

        # Se passar todas as verificações, retorna True e None (nenhum erro)
        return True, None
        
    @staticmethod
    def validate_password(password):
        """
        Valida se a senha fornecida atende aos critérios mínimos de segurança.

        Parâmetros:
        password (str): A senha a ser validada.

        Retorna:
        tuple: (bool, str ou None)
            - True, None se a senha for válida
            - False, mensagem de erro se a senha for inválida ou ausente

        Regras de validação:
        - Obrigatória não pode estar vazia
        - Mínimo de 6 caracteres
        - Deve conter pelo menos uma letra e um número
        """
        if not password:
        # Se nenhuma senha foi fornecida, retorna False e a mensagem de erro
            return False, "Senha é obrigatória"

        if len(password) < 6:
        # Se a senha tiver menos de 6 caracteres, retorna False e a mensagem de erro
            return False, "Senha deve ter ao menos 6 caracteres"

        # Verifica se a senha contém pelo menos uma letra e um número
        if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        # Se faltar letra ou número, retorna False e a mensagem de erro
            return False, "Senha deve conter letras e números"

        # Se passar todas as verificações, retorna True e None (nenhum erro)
        return True, None