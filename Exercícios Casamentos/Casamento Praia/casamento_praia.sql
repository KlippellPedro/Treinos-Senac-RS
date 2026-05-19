-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 15/04/2026 às 21:57
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `casamento_praia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `acesso_area`
--

CREATE TABLE `acesso_area` (
  `id_acesso` int(11) NOT NULL,
  `id_convidado` int(11) DEFAULT NULL,
  `id_area` int(11) DEFAULT NULL,
  `data_hora_acesso` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `acesso_area`
--

INSERT INTO `acesso_area` (`id_acesso`, `id_convidado`, `id_area`, `data_hora_acesso`) VALUES
(1, 1, 1, '2026-04-15 17:38:13'),
(2, 2, 3, '2026-04-15 17:38:13'),
(3, 3, 2, '2026-04-15 17:38:13');

-- --------------------------------------------------------

--
-- Estrutura para tabela `area`
--

CREATE TABLE `area` (
  `id_area` int(11) NOT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `nome_area` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `area`
--

INSERT INTO `area` (`id_area`, `id_evento`, `nome_area`) VALUES
(1, 1, 'Espaço da Cerimonia'),
(2, 1, 'Espaço da Recepção'),
(3, 1, 'Espaço de Festa'),
(4, 1, 'Cerimoia'),
(5, 1, 'Recepção'),
(6, 1, 'Festa');

-- --------------------------------------------------------

--
-- Estrutura para tabela `checkin`
--

CREATE TABLE `checkin` (
  `id_checkin` int(11) NOT NULL,
  `id_convidado` int(11) DEFAULT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `data_hora` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `checkin`
--

INSERT INTO `checkin` (`id_checkin`, `id_convidado`, `id_evento`, `data_hora`) VALUES
(1, 1, 1, '2026-04-15 14:35:37'),
(2, 2, 1, '2026-04-15 14:35:37'),
(3, 3, 1, '2026-04-15 14:35:37');

-- --------------------------------------------------------

--
-- Estrutura para tabela `convidado`
--

CREATE TABLE `convidado` (
  `id_convidado` int(11) NOT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `nome` varchar(150) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `codigo_qr` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `convidado`
--

INSERT INTO `convidado` (`id_convidado`, `id_evento`, `nome`, `tipo`, `codigo_qr`) VALUES
(1, 1, 'Miguel', 'Familia', '5425381310'),
(2, 1, 'Ryan', 'Amigos', '8615546017'),
(3, 1, 'Manuella', 'Amigos', '4683588367'),
(4, 1, 'Alexia', 'Familia', '2144143475'),
(5, 1, 'Eduardo', 'Familia', '8793804346'),
(6, 1, 'Sabrina', 'Amigos', '9064350342'),
(7, 1, 'Augusto', 'Familia', '2500179359'),
(8, 1, 'Gael', 'Equipe', '2200026820'),
(9, 1, 'Maria Júlia', 'Amigos', '7842155731'),
(10, 1, 'Rebeca', 'Equipe', '9413484950'),
(11, 1, 'Maria Alice', 'Familia', '3037823115'),
(12, 1, 'Yago', 'Amigos', '9415086809'),
(13, 1, 'Arthur', 'Amigos', '6543639359'),
(14, 1, 'Matheus', 'Amigos', '4533977957'),
(15, 1, 'Maria Vitória', 'Equipe', '9610654323'),
(16, 1, 'Benicio', 'Equipe', '2551143634'),
(17, 1, 'Cauã', 'Equipe', '8514318430'),
(18, 1, 'Bella', 'Amigos', '845805812'),
(19, 1, 'José Miguel', 'Familia', '6047861807'),
(20, 1, 'Mateus', 'Equipe', '5751358413'),
(21, 1, 'Vitor Hugo', 'Equipe', '5870879090'),
(22, 1, 'Lucca', 'Equipe', '4894092353'),
(23, 1, 'Maria Julia', 'Familia', '2188144022'),
(24, 1, 'Henry', 'Amigos', '489216700'),
(25, 1, 'Enzo', 'Equipe', '4397780619'),
(26, 1, 'Valentina', 'Amigos', '4377115197'),
(27, 1, 'Ana Clara', 'Familia', '2074638173'),
(28, 1, 'João Guilherme', 'Equipe', '2693590057'),
(29, 1, 'Enzo Gabriel', 'Familia', '1854732134'),
(30, 1, 'Diego', 'Familia', '30999105');

-- --------------------------------------------------------

--
-- Estrutura para tabela `evento`
--

CREATE TABLE `evento` (
  `id_evento` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `local` varchar(150) DEFAULT NULL,
  `data_evento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `evento`
--

INSERT INTO `evento` (`id_evento`, `nome`, `local`, `data_evento`) VALUES
(1, 'Casamento na praia', 'Skypia', '2026-05-28');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `perfil` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nome`, `cpf`, `email`, `senha`, `perfil`) VALUES
(1, 'Administrador', '06566581074', 'admin@wedding.com', '$2b$12$HkESHBYyAmTiYlgDVdJQGucaUzWsf5ZmE2HfI9om5/G0qE8uUqSGi', 'Admin'),
(2, 'Cerimonial', '83455794491', 'cerimonia@wedding.com', '$2b$12$vWAkDgt6Bgdxca7xCuC7a.jXe4JXlKmIaNy4FmKNr6w7/oNgl7gze', 'Comum');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario_evento`
--

CREATE TABLE `usuario_evento` (
  `id_usuario_evento` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_evento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario_evento`
--

INSERT INTO `usuario_evento` (`id_usuario_evento`, `id_usuario`, `id_evento`) VALUES
(1, 1, 1),
(2, 2, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `acesso_area`
--
ALTER TABLE `acesso_area`
  ADD PRIMARY KEY (`id_acesso`),
  ADD KEY `id_convidado` (`id_convidado`),
  ADD KEY `id_area` (`id_area`);

--
-- Índices de tabela `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`id_area`),
  ADD KEY `id_evento` (`id_evento`);

--
-- Índices de tabela `checkin`
--
ALTER TABLE `checkin`
  ADD PRIMARY KEY (`id_checkin`),
  ADD KEY `id_convidado` (`id_convidado`),
  ADD KEY `id_evento` (`id_evento`);

--
-- Índices de tabela `convidado`
--
ALTER TABLE `convidado`
  ADD PRIMARY KEY (`id_convidado`),
  ADD UNIQUE KEY `codigo_qr` (`codigo_qr`),
  ADD KEY `id_evento` (`id_evento`);

--
-- Índices de tabela `evento`
--
ALTER TABLE `evento`
  ADD PRIMARY KEY (`id_evento`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Índices de tabela `usuario_evento`
--
ALTER TABLE `usuario_evento`
  ADD PRIMARY KEY (`id_usuario_evento`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_evento` (`id_evento`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `acesso_area`
--
ALTER TABLE `acesso_area`
  MODIFY `id_acesso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `area`
--
ALTER TABLE `area`
  MODIFY `id_area` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `checkin`
--
ALTER TABLE `checkin`
  MODIFY `id_checkin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `convidado`
--
ALTER TABLE `convidado`
  MODIFY `id_convidado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de tabela `evento`
--
ALTER TABLE `evento`
  MODIFY `id_evento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `usuario_evento`
--
ALTER TABLE `usuario_evento`
  MODIFY `id_usuario_evento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `acesso_area`
--
ALTER TABLE `acesso_area`
  ADD CONSTRAINT `acesso_area_ibfk_1` FOREIGN KEY (`id_convidado`) REFERENCES `convidado` (`id_convidado`) ON DELETE CASCADE,
  ADD CONSTRAINT `acesso_area_ibfk_2` FOREIGN KEY (`id_area`) REFERENCES `area` (`id_area`) ON DELETE CASCADE;

--
-- Restrições para tabelas `area`
--
ALTER TABLE `area`
  ADD CONSTRAINT `area_ibfk_1` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE;

--
-- Restrições para tabelas `checkin`
--
ALTER TABLE `checkin`
  ADD CONSTRAINT `checkin_ibfk_1` FOREIGN KEY (`id_convidado`) REFERENCES `convidado` (`id_convidado`) ON DELETE CASCADE,
  ADD CONSTRAINT `checkin_ibfk_2` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE;

--
-- Restrições para tabelas `convidado`
--
ALTER TABLE `convidado`
  ADD CONSTRAINT `convidado_ibfk_1` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE;

--
-- Restrições para tabelas `usuario_evento`
--
ALTER TABLE `usuario_evento`
  ADD CONSTRAINT `usuario_evento_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  ADD CONSTRAINT `usuario_evento_ibfk_2` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
