-- =============================
-- Banco de Dados: senac_wedding
-- =============================
CREATE DATABASE IF NOT EXISTS senac_wedding
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE senac_wedding;

-- =============================
-- Tabela: Perfil
-- =============================
CREATE TABLE IF NOT EXISTS perfil (
    id_perfil INT AUTO_INCREMENT PRIMARY KEY,
    nome_perfil VARCHAR(50) UNIQUE NOT NULL,
    descricao TEXT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Evento
-- =============================
CREATE TABLE IF NOT EXISTS evento (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome_evento VARCHAR(255) NOT NULL,
    data_evento DATE NOT NULL,
    local_evento VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Usuario
-- =============================
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    id_perfil INT NOT NULL,
    FOREIGN KEY (id_perfil) REFERENCES perfil(id_perfil)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Grupo
-- =============================
CREATE TABLE IF NOT EXISTS grupo (
    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
    nome_grupo VARCHAR(100) UNIQUE NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Convidado
-- =============================
CREATE TABLE IF NOT EXISTS convidado (
    id_convidado INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(255),
    numero_mesa INT,
    tipo_convidado ENUM('Familia','Amigos','Equipe Tecnica','Noivos') NOT NULL,

   
    status ENUM('pendente','confirmado') DEFAULT 'pendente',

    FOREIGN KEY (id_evento) REFERENCES evento(id_evento) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Convidado_Grupo (N:N)
-- =============================
CREATE TABLE IF NOT EXISTS convidado_grupo (
    id_convidado INT NOT NULL,
    id_grupo INT NOT NULL,
    PRIMARY KEY (id_convidado, id_grupo),
    FOREIGN KEY (id_convidado) REFERENCES convidado(id_convidado) ON DELETE CASCADE,
    FOREIGN KEY (id_grupo) REFERENCES grupo(id_grupo) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Checkin
-- =============================
CREATE TABLE IF NOT EXISTS checkin (
    id_checkin INT AUTO_INCREMENT PRIMARY KEY,
    id_convidado INT NOT NULL,
    id_usuario INT NOT NULL,
    data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unico_checkin (id_convidado),

    FOREIGN KEY (id_convidado) REFERENCES convidado(id_convidado) ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- =============================
-- Tabela: Login_Log
-- =============================
CREATE TABLE IF NOT EXISTS login_log (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sucesso BOOLEAN NOT NULL,
    ip_usuario VARCHAR(45),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;