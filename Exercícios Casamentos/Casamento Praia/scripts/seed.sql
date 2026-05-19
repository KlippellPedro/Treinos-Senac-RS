-- SEED DO CASAMENTO NA PRAIA --

INSERT INTO usuario (nome, cpf, email, senha, perfil) VALUES
    ('Administrador', '06566581074', 'admin@wedding.com','$2b$12$ofXCuXK8LcomkUAxawF2CeDtmFeLT1vo1moN72C5ziXArMqyUFwwW','Admin'),
    ('Cerimonial','83455794491','cerimonia@wedding.com','$2b$12$xUQq5qiWb9Yjgm5IN4yLsO/lC3O22qo1uLHzZ4OdCyO/TRQ8jSvWO','Comum');
INSERT INTO evento (nome, local, data_evento) VALUES
    ('Casamento na praia', 'Skypia', '2026-05-28');
INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Espaço da Cerimonia'),
    (1, 'Espaço da Recepção'),
    (1, 'Espaço de Festa');
INSERT INTO usuario_evento (id_usuario, id_evento) VALUES
    (1, 1),
    (2, 1);
INSERT INTO convidado (id_evento, nome, tipo, codigo_qr) VALUES(1,'Kamilly','Familia','6624095038'),
(1,'Guilherme','Familia','3499619127'),
(1,'Antonella','Amigos','4764442507'),
(1,'Ágatha','Familia','7982323355'),
(1,'Diogo','Equipe','9806776113'),
(1,'Manuela','Equipe','3845308284'),
(1,'Caroline','Equipe','7057193778'),
(1,'Lavínia','Equipe','720863750'),
(1,'Lara','Familia','1363793224'),
(1,'Antony','Amigos','9405062342'),
(1,'Pedro Lucas','Amigos','8790251197'),
(1,'Arthur','Familia','7651077380'),
(1,'Anna Liz','Amigos','9798380152'),
(1,'Bianca','Equipe','7260028381'),
(1,'Mariah','Amigos','1814693221'),
(1,'João Pedro','Amigos','3154615870'),
(1,'Cecília','Amigos','1453252778'),
(1,'Marcelo','Familia','8340987969'),
(1,'Leonardo','Equipe','4864584471'),
(1,'Cecilia','Familia','2905713801'),
(1,'Enzo','Familia','2458471425'),
(1,'Natália','Familia','8058724481'),
(1,'Mirella','Amigos','6194816781'),
(1,'Caroline','Equipe','4679567731'),
(1,'Laís','Familia','289275128'),
(1,'Lívia','Familia','635398721'),
(1,'Manuela','Equipe','2761025550'),
(1,'Sofia','Amigos','5369658911'),
(1,'Valentina','Familia','5542289582'),
(1,'Leandro','Familia','1777841392');
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
    