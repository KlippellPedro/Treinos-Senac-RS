from faker import Faker
import random
import bcrypt

fake=Faker('pt-BR')

def limpar_cpf(cpf:str):
    return "".join(filter(str.isdigit, cpf))

def gerar_hash(senha:str):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def gerar_sql(qtd_convidados:int)->str:
    sql="-- SEED TREINO 1 --\n\n"

    sql+=f"""
INSERT INTO usuario (nome,email,cpf,senha,perfil) VALUES
('Administrador', 'amd@gmail.com', '06768372082', '{gerar_hash("Adminteste123")}', 'Admin');
"""
    sql+=f"""
INSERT INTO evento (id_evento, nome,data,local) VALUES
(1, 'Funeral do Senac Faculdade', '2020-10-01', 'Centro historico');
"""
    linhas=[]
    tipos=['Aluno', 'Professor', 'Equipe']
    stat=['Confirmado', 'Pendente', 'Cancelado']
    for i in range(qtd_convidados-2):
        nome=fake.first_name()
        email=fake.email()
        cpf=limpar_cpf(fake.cpf())
        telefone=fake.cellphone_number()
        tipo=random.choice(tipos)
        status=random.choice(stat)

        linhas.append(f"""('{nome}','{email}','{cpf}','{telefone}','{tipo}','{status}',1)""")
    
    sql+=f"""
INSERT INTO convidado (nome,email,cpf,telefone,tipo,status,id_evento) VALUES"""+ ",\n".join(linhas)+";\n"
    
    return sql

if __name__ == "__main__":
    while True:
        try:
            qtd=int(input("Quantos convidados deseja adicionar (min 30): "))
            if qtd>=30:
                break
            else:
                print("Digite um numero maior ou igual a 30")
        except:
            print("Porfavor insira um numero valido")
    sql=gerar_sql(qtd)

    with open("seed.sql", "w", encoding="utf-8") as f:
        f.write(sql)

    print("\nSeed gerado com sucesso!")