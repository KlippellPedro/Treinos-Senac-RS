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
    """Gera SQL completo para seed do banco Casamento no Sitio."""
    sql = "-- SEED DO CASAMENTO NO SITIO --\n\n"


    sql += f"""INSERT INTO usuario (nome, cpf, email, senha, perfil) VALUES
    ('Administrador', '75688329134', 'admin@wedding.com', '{gerar_hash("senhausuario1")}','Admin'),
    ('Cerimonial', '6357729145', 'recepcao@wedding.com', '{gerar_hash("senhausuario2")}','Comum');
    """

    sql += """INSERT INTO evento (nome, local, data_evento) VALUES
    ('Casamento no Sítio', 'Fenda do biquine', '2026-01-17');
    """

    sql += """INSERT INTO area (id_evento, nome_area, exige_vip) VALUES
    (1, 'Espaço do Buffet', 1),
    (1, 'Espaço de Danca', 1),
    (1, 'Espaço de Fotos', 1);
    """

    sql += """INSERT INTO usuario_evento (id_evento, id_usuario) VALUES
    (1, 1),
    (1, 2);
    """
    linhas = []
    categoria = ['Geral', 'Vip']
    stats=['Confirmado', 'Pendente', 'Cancelado']
    for _ in range(qtd_convidados):
        nome = fake.first_name().replace("'", "''")
        status= random.choice(stats)
        tipos = random.choice(categoria)
        linhas.append(f"""(1, '{nome}', '{status}','{tipos}')""")

    sql += """INSERT INTO convidado (id_evento, nome, status, categoria) VALUES""" + ",\n".join(linhas) + ";\n"

    sql += """INSERT INTO acesso_area (id_convidado, id_area, data_hora_acesso) VALUES
    (1, 1, NOW()),
    (1, 2, NOW()),
    (1, 3, NOW());
    """

    sql += """INSERT INTO checkin (id_convidado, id_usuario, id_evento, data_hora) VALUES
    (1, 1, 1, NOW()),
    (2, 1, 1, NOW()),
    (3, 1, 1, NOW());
    """

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