# Sistema de Gestão de Eventos e Check-in – Projeto "Senac Wedding"

## Introdução
### O que é e o que visa resolver
Este sistema web foi desenvolvido para gestão interna de eventos, focando na administração, controle de convidados e registro de check-ins. O público (convidados) não acessa diretamente o sistema; toda interação é mediada pelos microserviços. O sistema organiza a gestão em três perfis principais: **Administrador** e **Guest Manager** , garantindo segurança, controle de permissões e rastreabilidade das ações.

O exemplo do evento é o **Senac Wedding**, reunindo convidados divididos em setores como Família, Amigos, Equipe Técnica e Noivos. O sistema permite:  

• Cadastro e gerenciamento de usuários, convidados e grupos;  
• Registro de check-ins por usuários autorizados;  
• Visualização de dashboards com indicadores de presença e status dos convidados;  
• Controle de permissões por perfil de acesso.

O principal fluxo de funcionalidades do sistema inclui:  
• Cadastro e listagem de usuários, eventos e convidados;  
• Registro de check-in pelos validadores;  
• Relatórios de presença por evento e setor;  
• Controle de permissões por perfil.

---

## Lista de Funcionalidades

1. **Usuários e Perfis de Acesso**  
• Cadastro e gerenciamento de usuários (CRUD): Nome, CPF, e-mail, senha;  
• Perfis com permissões distintas: Administrador, Guest Manager, Validador.

2. **Gestão de Eventos e Convidados**  
• Cadastro de Eventos (CRUD): Nome, data, local;  
• Cadastro de Convidados (CRUD): Nome, sobrenome, CPF, e-mail, telefone, grupo e setor;  
• Cadastro de Grupos (CRUD);  
• Consulta de convidados por evento ou grupo;  
• Controle de status do convidado: pendente, confirmado, check-in.

3. **Check-in**  
• Registro de check-in manual pelo validador;  
• Registro vinculado ao usuário que realizou o check-in;  
• Status atualizado automaticamente e log de ações.

4. **Dashboards e Relatórios**  
• Visualização de presença por evento e setor;  
• Indicadores de convidados confirmados, pendentes ou validados;  
• Exportação de relatórios em CSV ou visualização em tabela.

5. **Autenticação e Controle de Acesso**  
• Tela de login: e-mail/CPF e senha;  
• Controle de permissões por perfil;  
• Geração de tokens JWT para validação de sessão.

---

## Protótipo (Figma)
Você pode acessar o protótipo do sistema neste link:  
[Protótipo Senac Wedding]()

Você pode decidir qual perfil utilizar na hora do acesso pela barra lateral esquerda.

---

## Pré-requisitos
1. **XAMPP** (porta MySQL aberta)  
2. **Python 3.10+** (recomenda-se criar venv)  
3. **Git** (para clonar o repositório)  
4. **MySQL** (SGBD utilizado)  
5. Instalação das dependências Python via `requirements.txt` de cada microserviço

---

## Instruções de Uso
1. Ative a porta MySQL do XAMPP e importe o banco de dados:
cd Senac-Wedding
Crie e ative o ambiente virtual:
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instale as dependências de cada microserviço:
pip install -r services/auth_service/requirements.txt
pip install -r services/checkin_service/requirements.txt
pip install -r services/guest_service/requirements.txt
pip install -r services/user_service/requirements.txt

# Execute os serviços (cada run.py) em terminais separados:
python services/auth_service/run.py
python services/checkin_service/run.py
python services/guest_service/run.py
python services/user_service/run.py

# Principais Páginas
Log-in - http://localhost:5000/
Usuários - http://localhost:5000/usuarios
Eventos (Admin) - http://localhost:5000/eventos-admin
Eventos limitado (Guest Manager) - http://localhost:5000/eventos
Tela de Check-in (Validador) - http://localhost:5000/checkin

# Clone o repositório:
git clone https://github.com/seu-usuario/Senac-Wedding.git

# Perfis
## Administrador

Responsabilidades

Gerencia usuários, eventos, convidados e grupos;
Acompanha check-ins e relatórios;
Acessa a Dashboard;
Permite realizar alterações administrativas gerais.


#### Dados para teste de log-in
E-mail: admin@wedding.com </br>
Senha: Admin@teste.com123

## Guest Manager

Responsabilidades

Gerencia convidados e grupos;
Realiza reservas ou atualizações de status de convidados;
Registra check-ins manualmente pelo código do convidado;
Atualiza status e mantém log de ações;
Não acessa funcionalidades de Admin.

#### Dados para teste de log-in
E-mail: recepcao@wedding.com

Senha: Recepcao@teste.com123


## Técnologias e bibliotecas implementadas (e suas versões)
- Flask: ^2.3.4
- SQLAlchemy: ^2.0.23
- PyMySQL: ^1.0.3
- JWT: ^2.6.0
- bcrypt: ^4.0.1
- requests: ^2.32.0
- pandas: ^2.1.0
- python-dotenv: ^1.0.0
- pytest: ^8.0.1