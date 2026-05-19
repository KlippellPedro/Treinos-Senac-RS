from faker import Faker
import random
import bcrypt


fake = Faker('pt_BR')


def limpar_cpf(cpf: str) -> str:
    """Remove qualquer caractere que não seja número do CPF."""
    return ''.join(filter(str.isdigit, cpf))


def gerar_hash(senha: str) -> str:
    """Gera hash bcrypt para a senha."""
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def gerar_sql(qtd_convidados: int) -> str:
    """Gera SQL completo para seed do banco Senac Wedding."""
    sql = "-- SEED OFICIAL PROVA SENAC WEDDING\n\n"

 
    sql += """
INSERT INTO perfil (id_perfil, nome_perfil) VALUES
(1, 'Admin'),
(2, 'Recepção');
"""

    sql += """
INSERT INTO buffet (id_buffet, tipo_buffet) VALUES
(1, 'Livre'),
(2, 'Vip');
"""


    sql += f"""
INSERT INTO usuario (nome, cpf, email, senha, id_perfil) VALUES
('Administrador', '12345678901', 'admin@wedding.com', '{gerar_hash("admin123")}', 1),
('Cerimonial', '10987654321', 'recepcao@wedding.com', '{gerar_hash("123456")}', 2);
"""


    sql += """
INSERT INTO evento (id_evento, nome_evento, data_evento, local_evento) VALUES
(1, 'Casamento Senac Wedding', '2026-12-20', 'Hotel Cambará');
"""

    linhas = []


    linhas.append(f"""(
        1,
        'João',
        'Silva',
        '11111111111',
        '(51) 99999-0001',
        'noivo@email.com',
        1,
        'Noivos'
    )""")
    linhas.append(f"""(
        1,
        'Maria',
        'Silva',
        '22222222222',
        '(51) 99999-0002',
        'noiva@email.com',
        1,
        'Noivos'
    )""")

 
    tipos = ['Família', 'Amigos', 'Equipe Técnica']
    for _ in range(qtd_convidados - 2):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        cpf = limpar_cpf(fake.cpf())
        telefone = fake.phone_number()
        email = fake.email()
        numero_mesa = random.randint(1, 20)
        tipo_convidado = random.choice(tipos)
        linhas.append(f"""(
        1,
        '{nome}',
        '{sobrenome}',
        '{cpf}',
        '{telefone}',
        '{email}',
        {numero_mesa},
        '{tipo_convidado}'
    )""")

    sql += """
INSERT INTO convidado 
(id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado)
VALUES
""" + ",\n".join(linhas) + ";\n"

    return sql


if __name__ == "__main__":

    while True:
        try:
            qtd = int(input("Quantidade de convidados (mín 30): "))
            if qtd >= 30:
                break
            else:
                print("Informe um número maior ou igual a 30.")
        except ValueError:
            print("Por favor, insira um número válido.")

    sql = gerar_sql(qtd)

  
    with open("seed.sql", "w", encoding="utf-8") as f:
        f.write(sql)

    print("Seed gerado com sucesso!")