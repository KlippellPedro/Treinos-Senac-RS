-- SEED DO CASAMENTO NA PRAIA --

INSERT INTO usuario (nome, cpf, email, senha, perfil) VALUES
    ('Bento','60812479530','raul49@example.net','$2b$12$t46q0Ur6CTu1fkfP7m7saO0FyX2ZakrS0zsUGl6YRR5O.t3hvsoWu','Admin'),
    ('Ana Júlia','45790261361','costaenrico@example.net','$2b$12$eri3QtAtnV.j8x1SCtOSYuZI4yreoMWHX3gn0d7dWk/FxIFeOUcYS','Comum');
    INSERT INTO evento (nome, data_evento, tipo_evento, pais, estado, cidade, bairro, rua, numero, complemento) VALUES
    ('Casamento na praia', '2023-08-15', 'Casamento','Suécia','('CE', 'Ceará')', 'Pacheco', 'Santa Monica', 'Peixoto do Campo', '44', 'Ao lado de um restaurante');
    INSERT INTO area (id_evento, nome_area) VALUES
    (1, 'Espaço da Cerimonia'),
    (1, 'Espaço da Recepção'),
    (1, 'Espaço de Festa');
    INSERT INTO usuario_evento (id_usuario, id_evento) VALUES
    (1, 1),
    (2, 1);
    INSERT INTO convidado (id_evento, nome, tipo, codigo_qr) VALUES(1,'Ana Luiza','Amigos','7124802104'),
(1,'Maria Alice','Equipe','5550316404'),
(1,'Sophie','Equipe','2884897231'),
(1,'Diego','Familia','5381654360'),
(1,'Dante','Familia','377859423'),
(1,'Gabrielly','Familia','6792511008'),
(1,'Bruno','Amigos','3039262012'),
(1,'Luísa','Familia','5233751156'),
(1,'Felipe','Amigos','9933312061'),
(1,'Eloá','Familia','7263399179'),
(1,'Nina','Amigos','3213354477'),
(1,'Otto','Familia','9796772834'),
(1,'Maria Sophia','Familia','9782372594'),
(1,'Raul','Equipe','1880045798'),
(1,'Elisa','Familia','1203877196'),
(1,'Ester','Familia','2350914953'),
(1,'Milena','Equipe','8243499770'),
(1,'Nicole','Amigos','7833796511'),
(1,'Gael Henrique','Equipe','66325426'),
(1,'Rhavi','Amigos','1092105638'),
(1,'Pietro','Familia','8182735527'),
(1,'Clara','Familia','5673786251'),
(1,'Marcelo','Equipe','1152269545'),
(1,'Ayla','Amigos','5119753820'),
(1,'Ana Beatriz','Equipe','1367304390'),
(1,'Ana Laura','Equipe','8965428033'),
(1,'Antônio','Familia','7012876892'),
(1,'Maria Liz','Equipe','4814354338'),
(1,'Evelyn','Equipe','5420505258'),
(1,'Arthur','Familia','7916871372');
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
    