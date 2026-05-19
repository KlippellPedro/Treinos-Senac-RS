from faker import Faker
import random
import bcrypt


fake = Faker('pt_BR')


def limpar_cpf(cpf: str):
    return ''.join(filter(str.isdigit, cpf))


def gerar_hash(senha: str): 
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')




def gerar_sql(qtd_convidados: int) -> str:
    sql = "-- SEED  WEDDING\n\n"

    sql += """
INSERT INTO perfil (id_perfil, nome_perfil) VALUES
(1, 'Admin'),
(2, 'Recepcao');
"""


    sql += f"""
INSERT INTO usuario (nome, cpf, email, senha, id_perfil) VALUES
('Administrador', '12345678901', 'admin@wedding.com', '{gerar_hash("Admin@teste.com123")}', 1),
('Cerimonial', '10987654321', 'recepcao@wedding.com', '{gerar_hash("Recepcao@teste.com123")}', 2);
"""

    # print("\n=== SENHAS PARA TESTE ===")
    # print(f"Administrador (admin@wedding.com): {"Admin@teste.com123"}")
    # print(f"Cerimonial (recepcao@wedding.com): {"Recepcao@teste.com123"}")

    sql += """
INSERT INTO evento (id_evento, nome_evento, data_evento, local_evento) VALUES
(1, 'Casamento Senac Wedding', '2026-12-20', 'Hotel Cambará');
"""

    linhas = []
    cpfs_usados = set()

    def cpf_unico():
        while True:
            cpf = limpar_cpf(fake.cpf())
            if cpf not in cpfs_usados:
                cpfs_usados.add(cpf)
                return cpf

    linhas.append(f"""(
        1,
        'Joao',
        'Silva',
        '11111111111',
        '(51)999990001',
        'noivo@email.com',
        1,
        'Noivos',
        'confirmado'
    )""")

    linhas.append(f"""(
        1,
        'Maria',
        'Silva',
        '22222222222',
        '(51)999990002',
        'noiva@email.com',
        1,
        'Noivos',
        'confirmado'
    )""")

    tipos = ['Familia', 'Amigos', 'Equipe Tecnica']

    for i in range(qtd_convidados - 2):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        cpf = cpf_unico()
        telefone = fake.phone_number().replace(" ", "").replace("-", "")
        email = fake.email()
        numero_mesa = random.randint(1, 20)
        tipo_convidado = random.choice(tipos)

        status = 'confirmado' if random.random() < 0.3 else 'pendente'

        linhas.append(f"""(
        1,
        '{nome}',
        '{sobrenome}',
        '{cpf}',
        '{telefone}',
        '{email}',
        {numero_mesa},
        '{tipo_convidado}',
        '{status}'
    )""")

    sql += """
INSERT INTO convidado 
(id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado, status)
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

    print("\nSeed gerado com sucesso!")