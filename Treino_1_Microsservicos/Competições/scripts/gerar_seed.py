from faker import Faker
import random
import bcrypt
import binascii

class Config:
    LOCALE='pt_BR'
    SENHA_TAMANHO=8

class PasswordService:
    @staticmethod
    def gerar_hash(senha: str)-> str:
        return bycrypt.
    
    # Falata terminar

class FakerService:
    def __init__(self, locale:str):
        self.fake=Faker(locale)

    def nome(self): return self.fake.first_name()
    def sobrenome(self): return self.fake.last_name()
    def cpf(self): return self.fake.cpf().replace('-','').replace('.','')
    def telefone(self): return self.fake.phone_number()
    def email(self): return self.fake.email()
    def nome_completo(self): return self.fake.name()

class SQLBuilder:
    def __init__(self):
        self.commands=[]
    
    def add(self,command:str):
        self.commands.append(command)
    
    def build(self):
        return "\n".join(self.commands)
    

class SeedGenerator:
    def __init__(self, qtd_convidados:int):
        self.faker= FakerService(Config.LOCALE)
        self.sql= SQLBuilder()
        self.senhas_geradas={}
        self.qtd_convidados=qtd_convidados
        self.evento_id=1
    
    def gerar_perfis(self):
        perfis=[
            ('Administrador', 'usuario com todos os privilégios'),
            ('Cerimonialista', 'usuario responsável pelo evento')
        ]
        for idx, (nome,desc) in enumerate(perfis,start=1):
            self.sql.add(f"INSERT INTO perfil (id_perfil, nome_perfil, descricao) VALUES ({idx}, '{nome}', '{desc}');")

    def gerar_evento(self):
        self.sql.add(f"""
INSERT INTO evento (id_evento, nome_completo, data_evento, local_evento)
VALUES ({self.evento_id}, 'casamento João e Maria', '2026-12-10', 'Salão Principal');
""")
        
    def gerar_usuario(self):
        senha_admin= PasswordService.gerar_senha_aleatoria(Config.SENHA_TAMANHO)
        senha_cerimonial=PasswordService.gerar_senha_aleatoria(Config.SENHA_TAMANHO)
        self.senhas_geradas['admin@wedding.com']= senha_admin
        self.senhas_geradas['cerimonial@wedding.com']=senha_cerimonial

        hash_admin= PasswordService.gerar_hash(senha_admin)
        hash_cerimonial=PasswordService.gerar_hash(senha_cerimonial)

        self.sql.add(f"""
INSERT INTO usuario (nome, cpf, email, senha, id_perfil) VALUES
('{self.faker.nome_completo()}', '{self.faker.cpf()}', 'admin@wedding.com', '{hash_admin}', 1),
('{self.faker.nome_completo()}', '{self.faker.cpf()}', 'cerimonial@wedding.com', '{hash_cerimonial}', 2),
""")
        
    def gerar_grupos(self):
        grupos= ['Familia', 'Amigos', 'Equipe Técnica']
        for g in grupos:
            self.sql.add(f"INSERT INTO grupo (nome_grupo) VALUES ('{g}');")
        
    def gerar_convidados(self):
        tipos=['Familia', 'Amigos', 'Equipe Técnica']

        linhas=[]

        linhas.append(f"({self.evento_id}, 'Noivo', 'João','12345678901', '(11) 9999-8888', 'noivo@wedding.com',1,'Noivos')")
        linhas.append(f"({self.evento_id}, 'Noivo', 'João','12345678901', '(11) 8888-9999', 'noiva@wedding.com',1,'Noivos')")

        for _ in range(self.qtd_convidados -2):
            nome=self.faker.nome()
            sobrenome=self.faker.sobrenome()
            cpf=self.faker.cpf()
            telefone=self.faker.telefone()
            email=self.faker.cpf()
            mesa=random.randint(1,20)
            tipo=random.choice(tipos)
            linhas.append(f"({self.evento_id},'{nome}','{sobrenome}','{cpf}','{telefone}','{telefone}','{email}',{mesa},'{tipo}')")
        
        query= "INSERT INTO convidado (id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa,tipo_convidado) VALUES\n"
        query += ",\n".join(linhas)+";"
        self.sql.add(query)

    def gerar_convidado_grupo(self):
        for cid in range(1, self.qtd_convidados+1):
            grupo_id=random.randint(1,3)
            self.sql.add(f"INSERT INTO convidado_grupo (id_convidado, id_grupo) VALUES ({cid}, {grupo_id});")
    
    def gerar(self):
        self.sql.add("-- =======================")
        self.sql.add("-- SEED GERADO AUTOMATICAMENTE")
        self.sql.add("-- =======================")

        self.gerar_perfis()
        self.gerar_evento()
        self.gerar_usuario()
        self.gerar_convidados()
        self.gerar_convidado_grupo()

        return self.sql.build()
    
if __name__=="__main__":
    while True:
        try:
            qtd=int(input("Quantos convidados deseja gerar? "))
            if qtd <=2:
                raise ValueError("O número minimo de convidados é 2 (os noivos).")
            break
        except ValueError as e:
            print(f"Digite um número inteiro válido. {e}")

    generator= SeedGenerator(qtd)
    sql_output=generator.gerar()

    with open("seed.sql", "w", encoding="utf-8") as f:
        f.write(sql_output)

    print("\n-- SQL gerado e salvo em seed.sql --\n")
    print("-- Senhas geradas --")
    for email, senha in generator.senhas_geradas.items():
        print(f"{email}: {senha}") 