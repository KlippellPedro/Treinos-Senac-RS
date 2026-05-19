-- SEED DO CASAMENTO INTERNACIONAL
INSERT INTO usuario (nome,cpf,email,senha,perfil) VALUES
    ('Administrador', '06566581074', 'admin@wedding.com','$2b$12$W62x9VLqsoYhho62nU6.v.97JrK85zIV8gQd2tZgxwuFhEBODCpgm','Admin'),
    ('Cerimonial','83455794491','cerimonia@wedding.com','$2b$12$3l8Q1xOqXX/tlRtNCySikORzhNXj63VDNXWctPYKuOsO48ptrFl6G','Comum');
INSERT INTO evento (nome,local,data_evento) VALUES
    ('Casamento internacional','México','2023-08-15');
INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Espaço da Hotelaria'),
    (1, 'Espaço da Recepção'),
    (1, 'Espaço de Cerimonia');
INSERT INTO usuario_evento (id_usuario, id_evento) VALUES
    (1, 1),
    (2, 1);
INSERT INTO convidado (id_evento, nome, nacionalidade, doc_status) VALUES(1,'Ana Cecília','Alemanha','Válido'),
(1,'Ana Carolina','França','Válido'),
(1,'Aurora','Espanha','Inválido'),
(1,'Alana','México','Válido'),
(1,'Ravi','França','Válido'),
(1,'João Felipe','Brasil','Válido'),
(1,'Vitor Gabriel','Alemanha','Inválido'),
(1,'Dante','Brasil','Válido'),
(1,'Ana Sophia','Espanha','Inválido'),
(1,'Melina','Alemanha','Inválido'),
(1,'Ágatha','Alemanha','Inválido'),
(1,'Vitória','Brasil','Inválido'),
(1,'Zoe','Espanha','Inválido'),
(1,'Gael','Brasil','Válido'),
(1,'Luiza','México','Inválido'),
(1,'João Pedro','Brasil','Válido'),
(1,'Lunna','EUA','Válido'),
(1,'João Pedro','EUA','Inválido'),
(1,'Lucas Gabriel','França','Válido'),
(1,'Alice','México','Inválido'),
(1,'Lavínia','EUA','Válido'),
(1,'Bianca','México','Válido'),
(1,'Luiz Henrique','Brasil','Válido'),
(1,'Francisco','Alemanha','Válido'),
(1,'Luiz Gustavo','França','Inválido'),
(1,'Rhavi','França','Inválido'),
(1,'Davi Lucca','França','Válido'),
(1,'Ana Luiza','México','Inválido'),
(1,'Vitor Gabriel','EUA','Inválido'),
(1,'Maria Liz','EUA','Inválido');
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
    