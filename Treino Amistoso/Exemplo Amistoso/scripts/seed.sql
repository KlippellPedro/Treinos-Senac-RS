-- SEED  WEDDING


INSERT INTO perfil (id_perfil, nome_perfil) VALUES
(1, 'Admin'),
(2, 'Recepcao');

INSERT INTO usuario (nome, cpf, email, senha, id_perfil) VALUES
('Administrador', '12345678901', 'admin@wedding.com', '$2b$12$PVGWohlvmLlIMD85hyJTcevpqh3RMTFrQYjIxWfMy.TKgTyzT5RJq', 1),
('Cerimonial', '10987654321', 'recepcao@wedding.com', '$2b$12$bhAOzXphRKJbiAHyBASv/OzhA/CjlNtRHkkU/S2Ohine17E.bYa7K', 2);

INSERT INTO evento (id_evento, nome_evento, data_evento, local_evento) VALUES
(1, 'Casamento Senac Wedding', '2026-12-20', 'Hotel Cambará');

INSERT INTO convidado 
(id_evento, nome, sobrenome, cpf, telefone, email, numero_mesa, tipo_convidado, status)
VALUES
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
        'Mariah',
        'Sousa',
        '93107268577',
        '+55(081)40369530',
        'mvargas@example.org',
        7,
        'Familia',
        'pendente'
    ),
(
        1,
        'Maria Luiza',
        'Teixeira',
        '87652349010',
        '5104939756',
        'isadora20@example.org',
        19,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Raul',
        'Costa',
        '42608539106',
        '(031)22047172',
        'luisaaragao@example.com',
        19,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Isaque',
        'Souza',
        '73192546034',
        '+556120798591',
        'luiz-miguel03@example.com',
        4,
        'Familia',
        'pendente'
    ),
(
        1,
        'Nathan',
        'Cardoso',
        '01938564766',
        '4138192056',
        'zvieira@example.com',
        5,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Cecília',
        'Marques',
        '86051297359',
        '+55(061)65760669',
        'upires@example.net',
        6,
        'Familia',
        'confirmado'
    ),
(
        1,
        'Maria Sophia',
        'Sales',
        '71936820595',
        '+55(084)07244486',
        'qrios@example.net',
        13,
        'Familia',
        'pendente'
    ),
(
        1,
        'Théo',
        'Pimenta',
        '06541823707',
        '6173684339',
        'ayllacarvalho@example.com',
        20,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'José',
        'Garcia',
        '86934017501',
        '+55(031)25008242',
        'ferreirajoana@example.net',
        4,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Dom',
        'Lopes',
        '35146890757',
        '+55(031)28409313',
        'gabrielapires@example.org',
        5,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Rebeca',
        'das Neves',
        '42395608700',
        '03003985640',
        'henry-gabrielsilva@example.net',
        3,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Ayla',
        'Cunha',
        '05728634117',
        '1193761258',
        'estermoreira@example.org',
        3,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Luiz Henrique',
        'Monteiro',
        '36517042890',
        '+55(061)24659671',
        'cda-rocha@example.com',
        18,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Kaique',
        'Almeida',
        '90154326780',
        '(031)29645463',
        'kamilly59@example.net',
        2,
        'Familia',
        'pendente'
    ),
(
        1,
        'Lucca',
        'Gomes',
        '12496085702',
        '(011)38094565',
        'dcamargo@example.net',
        11,
        'Familia',
        'confirmado'
    ),
(
        1,
        'Luana',
        'Campos',
        '32081569442',
        '(011)95966583',
        'barrosluigi@example.net',
        3,
        'Familia',
        'confirmado'
    ),
(
        1,
        'Theo',
        'Rocha',
        '72981406396',
        '5195946730',
        'aragaovalentina@example.org',
        18,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Ana Lívia',
        'Cavalcante',
        '93564021752',
        '+55(031)62024838',
        'duarteemilly@example.org',
        9,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Laís',
        'Santos',
        '23768915077',
        '(061)38100658',
        'saluiza@example.org',
        13,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Alícia',
        'Cirino',
        '84719563228',
        '+55(071)08937631',
        'fcamara@example.com',
        12,
        'Equipe Tecnica',
        'confirmado'
    ),
(
        1,
        'Zoe',
        'da Luz',
        '25837041680',
        '(021)08334433',
        'emanuella93@example.net',
        12,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Luara',
        'da Conceição',
        '95283706400',
        '(061)96028465',
        'henry69@example.org',
        15,
        'Amigos',
        'pendente'
    ),
(
        1,
        'João Pedro',
        'Carvalho',
        '32719584673',
        '7129072200',
        'fernandessabrina@example.com',
        1,
        'Familia',
        'confirmado'
    ),
(
        1,
        'Maria Isis',
        'Pacheco',
        '62490317822',
        '(031)57226364',
        'julia07@example.org',
        11,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Joaquim',
        'Machado',
        '42015897658',
        '(051)34849628',
        'castrohenry-gabriel@example.net',
        5,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Joana',
        'Nascimento',
        '62480173950',
        '+551140857317',
        'silveirazoe@example.com',
        6,
        'Amigos',
        'pendente'
    ),
(
        1,
        'Raquel',
        'Aparecida',
        '97268534191',
        '+55(051)32406720',
        'livia32@example.com',
        4,
        'Equipe Tecnica',
        'pendente'
    ),
(
        1,
        'Daniela',
        'Rezende',
        '57964208365',
        '+55(081)49396588',
        'maria-juliacavalcante@example.org',
        7,
        'Amigos',
        'confirmado'
    );
