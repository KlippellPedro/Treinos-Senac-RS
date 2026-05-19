from faker import Faker
import random
import bcrypt

fake = Faker('pt_BR')

class Usuario:
    def __init__(self, nome, cpf, email, senha, id_perfil):
        self.nome = nome
        self.cpf = self.limpar_cpf(cpf)
        self.email = email
        self.senha = self.gerar_hash(senha)
        self.id_perfil = id_perfil

    @staticmethod
    def limpar_cpf(cpf):
        return ''.join(filter(str.isdigit, cpf))

    @staticmethod
    def gerar_hash(senha):
        return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

class Convidado:
    cpfs_usados = set()

    def __init__(self, id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado, status):
        self.id_evento = id_evento
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = self.limpar_cpf(cpf)
        self.telefone = telefone
        self.email = email
        self.numero_mesa = numero_mesa
        self.tipo_convidado = tipo_convidado
        self.status = status

    @staticmethod
    def limpar_cpf(cpf):
        return ''.join(filter(str.isdigit, cpf))

    @classmethod
    def gerar_cpf_unico(cls):
        while True:
            cpf = cls.limpar_cpf(fake.cpf())
            if cpf not in cls.cpfs_usados:
                cls.cpfs_usados.add(cpf)
                return cpf

    @classmethod
    def gerar_aleatorio(cls, id_evento):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        cpf = cls.gerar_cpf_unico()
        telefone = fake.phone_number().replace(" ", "").replace("-", "")
        email = fake.email()
        numero_mesa = random.randint(1, 20)
        tipo_convidado = random.choice(['Familia', 'Amigos', 'Equipe Tecnica'])
        status = 'confirmado' if random.random() < 0.3 else 'pendente'
        return cls(id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado, status)

    def to_sql(self):
        return f"""(
        {self.id_evento},
        '{self.nome}',
        '{self.sobrenome}',
        '{self.cpf}',
        '{self.telefone}',
        '{self.email}',
        {self.numero_mesa},
        '{self.tipo_convidado}',
        '{self.status}'
    )"""


class GeradorSQL:
    def __init__(self, qtd_convidados):
        self.qtd_convidados = qtd_convidados
        self.convidados = []

    def gerar(self):
        sql = "-- SEED WEDDING\n\n"

        sql += """
            INSERT INTO perfil (id_perfil, nome_perfil) VALUES
            (1, 'Admin'),
            (2, 'Recepcao');
            """
        admin = Usuario("Administrador", "12345678901", "admin@wedding.com", "Admin@teste.com123", 1)
        recepcao = Usuario("Cerimonial", "10987654321", "recepcao@wedding.com", "Recepcao@teste.com123", 2)

        sql += f"""
            INSERT INTO usuario (nome, cpf, email, senha, id_perfil) VALUES
            ('{admin.nome}', '{admin.cpf}', '{admin.email}', '{admin.senha}', {admin.id_perfil}),
            ('{recepcao.nome}', '{recepcao.cpf}', '{recepcao.email}', '{recepcao.senha}', {recepcao.id_perfil});
            """

       
        sql += """
            INSERT INTO evento (id_evento, nome_evento, data_evento, local_evento) VALUES
            (1, 'Casamento Senac Wedding', '2026-12-20', 'Hotel Cambará');
            """

       
        self.convidados.append(Convidado(1, "Joao", "Silva", "11111111111", "(51)999990001", "noivo@email.com", 1, "Noivos", "confirmado"))
        self.convidados.append(Convidado(1, "Maria", "Silva", "22222222222", "(51)999990002", "noiva@email.com", 1, "Noivos", "confirmado"))

        
        for _ in range(self.qtd_convidados - 2):
            self.convidados.append(Convidado.gerar_aleatorio(1))

       
        sql += "INSERT INTO convidado (id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado, status) VALUES\n"
        sql += ",\n".join([c.to_sql() for c in self.convidados]) + ";\n"

        return sql


if __name__ == "__main__":
    while True:
        try:
            qtd = int(input("Quantidade de convidados (mín 30): "))
            if qtd >= 30:
                break
            print("Informe um número maior ou igual a 30.")
        except ValueError:
            print("Por favor, insira um número válido.")

    gerador = GeradorSQL(qtd)
    sql = gerador.gerar()

    with open("seed.sql", "w", encoding="utf-8") as f:
        f.write(sql)

    print("\nSeed gerado com sucesso!")