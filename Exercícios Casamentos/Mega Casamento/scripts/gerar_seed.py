from faker import Faker
import random
import bcrypt

fake= Faker('pt-BR')

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
    ('{fake.first_name()}','{limpar_cpf(fake.cpf())}','{fake.email()}','{gerar_hash("admin017")}','Admin'),
    ('{fake.first_name()}','{limpar_cpf(fake.cpf())}','{fake.email()}','{gerar_hash("cerimonial112")}','Comum');
    """
    sql+= f"""INSERT INTO evento (nome, data_evento, tipo_evento, pais, estado, cidade, bairro, rua, numero, complemento) VALUES
    ('Casamento no Senac', '2023-08-15', 'Casamento','{fake.country()}','{fake.state()}', '{fake.city()}', '{fake.bairro()}', '{fake.street_name()}', '{fake.building_number()}', '{random.choice(["Ao lado de um restaurante", "Ao lado de um bar", "Perto do mercado", "Do lado do rio",])}'),
    ('Festa de Aniversário', '2022-09-10', 'Aniversário','{fake.country()}','{fake.state()}', '{fake.city()}', '{fake.bairro()}', '{fake.street_name()}', '{fake.building_number()}', '{random.choice(["Ao lado de um restaurante", "Ao lado de um bar", "Perto do mercado", "Do lado do rio",])}'),
    ('Festa de Natal', '2027-12-25', 'Festa','{fake.country()}','{fake.state()}', '{fake.city()}', '{fake.bairro()}', '{fake.street_name()}', '{fake.building_number()}', '{random.choice(["Ao lado de um restaurante", "Ao lado de um bar", "Perto do mercado", "Do lado do rio",])}');
    """
    sql += """INSERT INTO area (id_evento, nome_area, exige_tipo) VALUES
    (1, 'Espaço da Cerimonia', 'Nenhum'),(1, 'Espaço da Recepção', 'Nenhum'),(1, 'Espaço da Festa', 'Nenhum'),(1, 'Espaço do OpenBar', '+18'),
    (2, 'Espaço do Parabens', 'Nenhum'),(2, 'Espaço Infantil', 'Nenhum'),(2, 'Espaço dos Lanches', 'nenhum'),
    (3, 'Espaço das Comidas', 'Nenhum'),(3, 'Espaço dos Presentes', 'Administração'),(3, 'Espaço do bar', '+18');
    """
    sql += """INSERT INTO usuario_evento (id_usuario, id_evento) VALUES
    (1, 1),(2, 1),(1, 2),(2, 2),(1, 3),(2, 3);
    """
    linhas=[]
    tipos=['Familia', 'Amigos', 'Equipe']
    for _ in range(qtd_convidados):
        nome=fake.first_name()
        tipo=random.choice(tipos)
        codigo_qr=fake.random_number(digits=10)
        linhas.append(f"(1,'{nome}','{tipo}','{codigo_qr}')")
    sql+="""INSERT INTO convidado (id_evento, nome, tipo, codigo_qr) VALUES"""+",\n".join(linhas)+";\n"
    
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