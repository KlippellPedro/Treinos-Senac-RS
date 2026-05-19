-- SEED DO CASAMENTO NA PRAIA --

INSERT INTO usuario (nome, cpf, email, senha, perfil) VALUES
    ('Administrador', '06566581074', 'admin@wedding.com','$2b$12$tn4hAufZEluSPMhjE.RwGemEYUFqtTEBz38VsKU.koWnPWAZm5gb6','Admin'),
    ('Cerimonial','83455794491','cerimonia@wedding.com','$2b$12$lgK47vnaHIFV0/AjgNIP6.7.8uMXMmI0D4pgzffdB65q5zrbu4WlC','Comum');
INSERT INTO evento (nome, local, data_evento) VALUES
    ('Wedding Urbano', 'Jardim Bôtanico', '2028-10-12');
INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Espaço da Cerimonia'),
    (1, 'Espaço da Recepção'),
    (1, 'Espaço da Festa');
INSERT INTO usuario_evento (id_usuario, id_evento) VALUES
    (1, 1),
    (2, 1);
INSERT INTO convidado (id_evento, nome, restricao) VALUES(1,'Maria Alice','Diabetico'),
(1,'Gael Henrique','Intolerante a lactose'),
(1,'Thales','Sem restrição'),
(1,'Maria Flor','Diabetico'),
(1,'Ágatha','Alergico a camarão'),
(1,'Natália','Vegetariano'),
(1,'João Vitor','Diabetico'),
(1,'Helena','Alergico a camarão'),
(1,'Felipe','Vegano'),
(1,'Luiz Fernando','Alergico a camarão'),
(1,'Alice','Intolerante a lactose'),
(1,'João Vitor','Intolerante a lactose'),
(1,'Brayan','Vegetariano'),
(1,'Ana Sophia','Alergico a camarão'),
(1,'Ana','Diabetico'),
(1,'Luiz Henrique','Sem restrição'),
(1,'Liam','Alergico a camarão'),
(1,'Maria','Diabetico'),
(1,'Marcela','Vegetariano'),
(1,'Dante','Alergico a camarão'),
(1,'Ester','Diabetico'),
(1,'Maria Luísa','Alergico a camarão'),
(1,'Jade','Diabetico'),
(1,'Ana Clara','Alergico a camarão'),
(1,'Gael','Vegano'),
(1,'Kamilly','Sem restrição'),
(1,'Caleb','Intolerante a lactose'),
(1,'Ana Beatriz','Intolerante a lactose'),
(1,'Ana','Alergico a camarão'),
(1,'Gabrielly','Intolerante a lactose'),
(1,'Caleb','Vegano'),
(1,'Vitor','Diabetico'),
(1,'Luan','Diabetico'),
(1,'Josué','Vegano'),
(1,'Giovanna','Sem restrição'),
(1,'Henry','Vegano'),
(1,'Stella','Vegano'),
(1,'Kamilly','Diabetico'),
(1,'João','Vegetariano'),
(1,'Vitória','Vegetariano'),
(1,'Bernardo','Intolerante a lactose'),
(1,'Maria Cecília','Vegetariano'),
(1,'Sophia','Alergico a camarão'),
(1,'Liz','Diabetico'),
(1,'Sophia','Diabetico'),
(1,'Bernardo','Alergico a camarão'),
(1,'Maria Júlia','Vegano'),
(1,'Antony','Alergico a camarão'),
(1,'Maria Cecília','Vegetariano'),
(1,'Lucca','Vegano');
INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Cerimoia'),
    (1, 'Recepção'),
    (1, 'Festa');
INSERT INTO acesso_area (id_convidado, id_area, data_hora_acesso) VALUES
    (1, 1, NOW()),
    (2, 3, NOW()),
    (3, 2, NOW());
INSERT INTO checkin (id_convidado, id_evento, data_hora) VALUES
    (1, 1, NOW()),
    (2, 1, NOW()),
    (3, 1, NOW());
    