from faker import Faker
import random
import bcrypt

fake= Faker('pt-br')

def limpar_cpf(cpf: str)->str:
    """Remove os caracteres que não sejam numero do cpf"""
    return ''.join(filter(str.isdigit,cpf))

def gerar_hash(senha:str)-> str:
    """gera o hash bcrypt para a senha """
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def gerar_sql(qtd_convidados: int)-> str:
    """Gera o sql do banco casamento_praia"""
    sql= "-- SEED DO CASAMENTO NA PRAIA --\n\n"

    sql += f"""INSERT INTO usuario (nome, cpf, email, senha, perfil) VALUES
    ('Administrador', '06566581074', 'admin@wedding.com','{gerar_hash("admin017")}','Admin'),
    ('Cerimonial','83455794491','cerimonia@wedding.com','{gerar_hash("cerimonial112")}','Comum');
    """
    sql+= f"""INSERT INTO evento (nome, local, data_evento) VALUES
    ('Casamento na praia', 'Skypia', '2026-05-28');
    """
    sql += """INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Espaço da Cerimonia'),
    (1, 'Espaço da Recepção'),
    (1, 'Espaço de Festa');
    """
    sql += """INSERT INTO usuario_evento (id_usuario, id_evento) VALUES
    (1, 1),
    (2, 1);
    """
    linhas=[]
    tipos=['Familia', 'Amigos', 'Equipe']
    for _ in range(qtd_convidados):
        nome=fake.first_name()
        tipo=random.choice(tipos)
        codigo_qr=fake.random_number(digits=10)
        linhas.append(f"(1,'{nome}','{tipo}','{codigo_qr}')")
    sql+="""INSERT INTO convidado (id_evento, nome, tipo, codigo_qr) VALUES"""+",\n".join(linhas)+";\n"
    
    sql+=f"""INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Cerimoia'),
    (1, 'Recepção'),
    (1, 'Festa');
    """
    sql+=f"""INSERT INTO acesso_area (id_convidado, id_area, data_hora_acesso) VALUES
    (1, 1, NOW()),
    (2, 3, NOW()),
    (3, 2, NOW());
    """ 
    sql+=f"""INSERT INTO checkin (id_convidado, id_evento, data_hora) VALUES
    (1, 1, NOW()),
    (2, 1, NOW()),
    (3, 1, NOW());
    """ 
    
    return sql

if __name__=="__main__":

    while True:
        try:
            qtd=int(input("Quantos convidados deseja cadastrar (mín 30): "))
            if qtd>=30:
                break
            else:
                print("Digite um numero maior que 30")
        except ValueError:
            print("Digite um número válido")
    sql=gerar_sql(qtd)
    with open("seed.sql", "w", encoding="utf-8") as f:
        f.write(sql)

    print("Seed gerado com sucesso!")