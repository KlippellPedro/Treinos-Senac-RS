-- SEED TREINO 1 --


INSERT INTO usuario (nome,email,cpf,senha,perfil) VALUES
('Administrador', 'amd@gmail.com', '06768372082', '$2b$12$50yd6t3lGO4jVzyEMxSQL.qas9wu3/MGSH6RX4V651tdUYGQOv5ai', 'Admin');

INSERT INTO evento (id_evento, nome,data,local) VALUES
(1, 'Funeral do Senac Faculdade', '2020-10-01', 'Centro historico');

INSERT INTO convidado (nome,email,cpf,telefone,tipo,status,id_evento) VALUES('Luiza','pietra40@example.com','06453189739','+55 (024) 90599 3043','Alunos','Pendente',1),
('Igor','limalorenzo@example.com','46830257956','+55 (23) 9 8807-9433','Alunos','Confirmado',1),
('Diogo','enzo-gabrielpinto@example.org','82649710322','+55 (069) 98247 4795','Alunos','Cancelado',1),
('Gabrielly','ravi-luccapimenta@example.com','75148632909','+55 (34) 94241 0472','Equipe','Confirmado',1),
('Dante','wcunha@example.com','89465370274','+55 77 9 0330 3920','Alunos','Confirmado',1),
('Henry Gabriel','imoura@example.com','04962137840','+55 21 92373-6893','Professores','Cancelado',1),
('Joaquim','wmontenegro@example.org','70126854335','+55 (95) 96052-7710','Alunos','Pendente',1),
('Ágatha','thales54@example.net','69351408205','+55 (05) 9 6808-9956','Alunos','Confirmado',1),
('Ana Julia','sousaana-livia@example.net','50831926406','+55 (21) 9 8953 9356','Professores','Pendente',1),
('Josué','carvalhojoao-pedro@example.net','61073948501','+55 (02) 96878-9854','Equipe','Confirmado',1),
('Vitória','qnovaes@example.net','47562310980','+55 71 96129 2070','Professores','Pendente',1),
('Cauã','rhavisouza@example.net','32154968791','+55 27 9 3983-6412','Professores','Pendente',1),
('Gabriel','joao-lucassilveira@example.com','39710526812','+55 (22) 93975 3497','Professores','Pendente',1),
('Melissa','maria-juliacampos@example.org','16520479802','+55 19 9 9774 2963','Professores','Pendente',1),
('Ana Julia','stellanunes@example.net','18649573282','+55 88 9 6404-7397','Professores','Pendente',1),
('Luara','juliada-cunha@example.com','45739602106','+55 (095) 99224 9055','Alunos','Confirmado',1),
('Clarice','pimentajoaquim@example.net','52486019324','+55 90 92104-6473','Equipe','Cancelado',1),
('Lívia','fonsecaravi@example.com','60759432856','+55 14 90120-4476','Professores','Cancelado',1),
('Alexandre','luana64@example.net','95236048133','+55 (90) 96991 7612','Professores','Pendente',1),
('Maria Alice','nicolaspacheco@example.org','21053489714','+55 (57) 9 4491 3112','Alunos','Cancelado',1),
('Ana Carolina','isabella26@example.net','47538902104','+55 (005) 95950-4876','Professores','Cancelado',1),
('Kamilly','wabreu@example.net','37194826500','+55 (34) 9 0157-7884','Equipe','Cancelado',1),
('Rafaela','yurirocha@example.com','39710568493','+55 40 9 1352-0099','Equipe','Cancelado',1),
('Marina','brayan64@example.org','25180934605','+55 71 91724-5619','Alunos','Cancelado',1),
('Maya','xrodrigues@example.com','62543798137','+55 (035) 99844-3179','Equipe','Cancelado',1),
('Eloah','camargomarcela@example.net','79240168567','+55 (40) 91612 9616','Equipe','Pendente',1),
('Murilo','henrique84@example.com','65924187373','+55 30 97753-0989','Equipe','Pendente',1),
('Daniel','andradeguilherme@example.com','39218405705','+55 56 9 1846 1646','Professores','Cancelado',1),
('Davi Luiz','matheusborges@example.org','39817652491','+55 (37) 93889 2288','Professores','Cancelado',1),
('Heloisa','ana-livia07@example.net','94203158788','+55 55 96218-2877','Alunos','Cancelado',1),
('Luiza','manuelapires@example.org','29185367095','+55 (54) 9 2676-6199','Alunos','Pendente',1),
('Luiz Felipe','lopesbella@example.net','19340652770','+55 21 94552 1287','Professores','Cancelado',1),
('Cauã','moreiradante@example.com','16239708577','+55 81 9 6808 7917','Equipe','Confirmado',1);
