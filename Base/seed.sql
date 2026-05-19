-- SEED WEDDING


            INSERT INTO perfil (id_perfil, nome_perfil) VALUES
            (1, 'Admin'),
            (2, 'Recepcao');
            
            INSERT INTO usuario (nome, cpf, email, senha, id_perfil) VALUES
            ('Administrador', '12345678901', 'admin@wedding.com', '$2b$12$t2hXTBIlO4D2mzsXTJk46O4.cZuCWKwHfdDn32TJdIb95Go3vsvl6', 1),
            ('Cerimonial', '10987654321', 'recepcao@wedding.com', '$2b$12$9ZBAn/AkiugpxTEg9/.H2.8tadmkNQK6TBprjLkH5eBTRAMYZ/Oz6', 2);
            
            INSERT INTO evento (id_evento, nome_evento, data_evento, local_evento) VALUES
            (1, 'Casamento Senac Wedding', '2026-12-20', 'Hotel Cambará');
            
            INSERT INTO convidado (id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado, status) VALUES
(
        1,
        'Joao',
        'Silva',
        '11111111111',
        '(51)999990001',
        'noivo@email.com',
        1,
        'Noivos',
        'confirmado'
    ),
(
        1,
        'Maria',
        'Silva',
        '22222222222',
        '(51)999990002',
        'noiva@email.com',
        1,
        'Noivos',
        'confirmado'
    ),
(
        1,
        'Eduarda',
        'Moraes',
        '43290186598',
        '7173975170',
        'ana-ceciliaaraujo@example.org',
        9,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Esther',
        'Borges',
        '97810452304',
        '+556157545333',
        'silvalais@example.com',
        15,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Diego',
        'Rocha',
        '03165947848',
        '(081)57987761',
        'aragaomaria-luisa@example.org',
        3,
        'Familia',
        'pendente'
    ),
(
        1,
        'Isadora',
        'Melo',
        '32548169006',
        '+55(061)67750152',
        'portomaria@example.org',
        13,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Yasmin',
        'Rios',
        '53014698270',
        '+557158767861',
        'marianeda-paz@example.com',
        8,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Gustavo Henrique',
        'Farias',
        '06239148750',
        '(051)83646097',
        'jmendonca@example.com',
        20,
        'Amigos',
        'confirmado'
    ),
(
        1,
        'Júlia',
        'Sá',
        '39518076448',
        '(041)36144531',
        'bsilveira@example.net',
        4,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Josué',
        'Farias',
        '85176493209',
        '+55(061)96645328',
        'tsa@example.com',
        10,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Lucas',
        'Teixeira',
        '12807396577',
        '+55(021)13755863',
        'joao-miguelalves@example.net',
        15,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Rodrigo',
        'Porto',
        '58213497023',
        '6128659977',
        'manuela28@example.org',
        10,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Arthur Gabriel',
        'Pinto',
        '96435720800',
        '(021)01773524',
        'helena81@example.org',
        19,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Brenda',
        'Melo',
        '49568710230',
        '(011)31716469',
        'freitasmaria-flor@example.com',
        5,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Arthur Gabriel',
        'Caldeira',
        '18954726011',
        '+55(031)06181961',
        'joao-vitor45@example.net',
        2,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Ana Lívia',
        'Teixeira',
        '96124735873',
        '+557126863275',
        'olivia61@example.com',
        1,
        'Familia',
        'pendente'
    ),
(
        1,
        'Maria Fernanda',
        'Farias',
        '37620491813',
        '(041)83876718',
        'ofernandes@example.com',
        11,
        'Familia',
        'pendente'
    ),
(
        1,
        'Ana Carolina',
        'da Mata',
        '14675983057',
        '+55(051)24269197',
        'carolinecamargo@example.org',
        14,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Davi Lucca',
        'Pastor',
        '35029874674',
        '3192536649',
        'vargascarolina@example.net',
        16,
        'Familia',
        'pendente'
    ),
(
        1,
        'Josué',
        'Gomes',
        '46379852000',
        '+552198363549',
        'gustavo-henrique11@example.com',
        4,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Pedro Lucas',
        'Garcia',
        '37268491069',
        '2179579228',
        'bcampos@example.net',
        13,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Henrique',
        'Montenegro',
        '51896037259',
        '4159076394',
        'beatrizcamargo@example.com',
        5,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Anthony',
        'Barros',
        '08439156766',
        '05007994643',
        'novaesfernanda@example.com',
        15,
        'Amigos',
        'confirmado'
    ),
(
        1,
        'Emanuelly',
        'Aparecida',
        '10785932488',
        '6177027465',
        'pnascimento@example.org',
        17,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'André',
        'Duarte',
        '54960218711',
        '3168291476',
        'agathada-mata@example.org',
        17,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Thales',
        'Brito',
        '24603795106',
        '+554140213355',
        'danteduarte@example.com',
        4,
        'Familia',
        'pendente'
    ),
(
        1,
        'Ana Júlia',
        'Farias',
        '52187946355',
        '+55(081)45405498',
        'zmoraes@example.com',
        11,
        'Familia',
        'confirmado'
    ),
(
        1,
        'Ravy',
        'Lopes',
        '68154072920',
        '(031)36419511',
        'lorena73@example.net',
        15,
        'Familia',
        'confirmado'
    ),
(
        1,
        'Enrico',
        'Guerra',
        '75904612885',
        '+55(084)50529388',
        'helenabarbosa@example.org',
        13,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'João Vitor',
        'Cardoso',
        '13294785682',
        '+55(071)65144377',
        'benicio81@example.org',
        14,
        'Familia',
        'pendente'
    );
