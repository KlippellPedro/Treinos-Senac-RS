-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16/04/2026 às 22:05
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
-- Banco de dados: `casamento_sitio`
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
(1, 1, 1, '2026-04-16 19:18:20'),
(2, 1, 2, '2026-04-16 19:18:20'),
(3, 1, 3, '2026-04-16 19:18:20');

-- --------------------------------------------------------

--
-- Estrutura para tabela `area`
--

CREATE TABLE `area` (
  `id_area` int(11) NOT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `nome_area` varchar(100) NOT NULL,
  `exige_vip` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `area`
--

INSERT INTO `area` (`id_area`, `id_evento`, `nome_area`, `exige_vip`) VALUES
(1, 1, 'Espaço do Buffet', 1),
(2, 1, 'Espaço de Danca', 1),
(3, 1, 'Espaço de Fotos', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `checkin`
--

CREATE TABLE `checkin` (
  `id_checkin` int(11) NOT NULL,
  `id_convidado` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `data_hora` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `checkin`
--

INSERT INTO `checkin` (`id_checkin`, `id_convidado`, `id_usuario`, `id_evento`, `data_hora`) VALUES
(1, 1, 1, 1, '2026-04-16 16:18:20'),
(2, 2, 1, 1, '2026-04-16 16:18:20'),
(3, 3, 1, 1, '2026-04-16 16:18:20');

-- --------------------------------------------------------

--
-- Estrutura para tabela `convidado`
--

CREATE TABLE `convidado` (
  `id_convidado` int(11) NOT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `nome` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `categoria` enum('Vip','Geral') DEFAULT 'Geral'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `convidado`
--

INSERT INTO `convidado` (`id_convidado`, `id_evento`, `nome`, `status`, `categoria`) VALUES
(31, 1, 'Stella', 'Confirmado', 'Geral'),
(32, 1, 'Matteo', 'Cancelado', 'Vip'),
(33, 1, 'Lucas Gabriel', 'Pendente', 'Vip'),
(34, 1, 'Isis', 'Cancelado', 'Geral'),
(35, 1, 'Samuel', 'Cancelado', 'Vip'),
(36, 1, 'Fernanda', 'Cancelado', 'Geral'),
(37, 1, 'Ana Laura', 'Cancelado', 'Vip'),
(38, 1, 'Samuel', 'Confirmado', 'Vip'),
(39, 1, 'Nicolas', 'Pendente', 'Vip'),
(40, 1, 'Erick', 'Cancelado', 'Vip'),
(41, 1, 'Raquel', 'Confirmado', 'Vip'),
(42, 1, 'Laís', 'Cancelado', 'Vip'),
(43, 1, 'Benício', 'Confirmado', 'Geral'),
(44, 1, 'Esther', 'Cancelado', 'Vip'),
(45, 1, 'Vitória', 'Cancelado', 'Geral'),
(46, 1, 'Oliver', 'Confirmado', 'Geral'),
(47, 1, 'Valentina', 'Confirmado', 'Geral'),
(48, 1, 'João Lucas', 'Confirmado', 'Geral'),
(49, 1, 'Júlia', 'Cancelado', 'Vip'),
(50, 1, 'Pedro Henrique', 'Cancelado', 'Geral'),
(51, 1, 'Calebe', 'Cancelado', 'Vip'),
(52, 1, 'Ana Vitória', 'Cancelado', 'Vip'),
(53, 1, 'Júlia', 'Pendente', 'Vip'),
(54, 1, 'Manuela', 'Cancelado', 'Geral'),
(55, 1, 'Renan', 'Confirmado', 'Vip'),
(56, 1, 'Ester', 'Pendente', 'Vip'),
(57, 1, 'Maria Eduarda', 'Confirmado', 'Geral'),
(58, 1, 'Milena', 'Pendente', 'Vip'),
(59, 1, 'Davi Luiz', 'Cancelado', 'Geral'),
(60, 1, 'Maria Isis', 'Cancelado', 'Vip'),
(61, 1, 'Leandro', 'Cancelado', 'Vip'),
(62, 1, 'Eloá', 'Pendente', 'Vip'),
(63, 1, 'Isabel', 'Pendente', 'Vip'),
(64, 1, 'Murilo', 'Cancelado', 'Vip'),
(65, 1, 'Ana Vitória', 'Pendente', 'Geral'),
(66, 1, 'Pedro Lucas', 'Pendente', 'Vip'),
(67, 1, 'Ísis', 'Pendente', 'Vip'),
(68, 1, 'Pietro', 'Confirmado', 'Geral'),
(69, 1, 'Juan', 'Pendente', 'Vip'),
(70, 1, 'Marcela', 'Pendente', 'Geral'),
(71, 1, 'Thales', 'Pendente', 'Vip'),
(72, 1, 'Gael', 'Cancelado', 'Vip'),
(73, 1, 'Fernando', 'Cancelado', 'Vip'),
(74, 1, 'Thiago', 'Pendente', 'Vip'),
(75, 1, 'Luiz Felipe', 'Cancelado', 'Geral'),
(76, 1, 'Otto', 'Pendente', 'Geral'),
(77, 1, 'Fernanda', 'Confirmado', 'Geral'),
(78, 1, 'Milena', 'Confirmado', 'Vip'),
(79, 1, 'Isis', 'Confirmado', 'Vip'),
(80, 1, 'Asafe', 'Pendente', 'Vip'),
(81, 1, 'Pedro', 'Cancelado', 'Vip'),
(82, 1, 'Thiago', 'Cancelado', 'Vip'),
(83, 1, 'Eloá', 'Cancelado', 'Vip'),
(84, 1, 'Catarina', 'Cancelado', 'Geral'),
(85, 1, 'Vitória', 'Confirmado', 'Geral'),
(86, 1, 'Guilherme', 'Cancelado', 'Geral'),
(87, 1, 'Felipe', 'Confirmado', 'Geral'),
(88, 1, 'Maria Alice', 'Pendente', 'Geral'),
(89, 1, 'Mathias', 'Confirmado', 'Vip'),
(90, 1, 'Ravi Lucca', 'Pendente', 'Geral'),
(91, 1, 'Alana', 'Cancelado', 'Geral'),
(92, 1, 'Emanuelly', 'Cancelado', 'Geral'),
(93, 1, 'Lorena', 'Pendente', 'Geral'),
(94, 1, 'Lunna', 'Cancelado', 'Vip'),
(95, 1, 'Levi', 'Confirmado', 'Geral'),
(96, 1, 'Luna', 'Cancelado', 'Geral'),
(97, 1, 'Ana', 'Cancelado', 'Geral'),
(98, 1, 'Ana Liz', 'Cancelado', 'Vip'),
(99, 1, 'Joaquim', 'Pendente', 'Geral'),
(100, 1, 'Maria Eduarda', 'Pendente', 'Geral'),
(101, 1, 'Lara', 'Pendente', 'Geral'),
(102, 1, 'Jade', 'Confirmado', 'Vip'),
(103, 1, 'Ravi Lucca', 'Pendente', 'Vip'),
(104, 1, 'Maya', 'Pendente', 'Geral'),
(105, 1, 'Maria Vitória', 'Confirmado', 'Geral'),
(106, 1, 'Oliver', 'Confirmado', 'Vip'),
(107, 1, 'Bruno', 'Cancelado', 'Vip'),
(108, 1, 'Cauã', 'Cancelado', 'Geral'),
(109, 1, 'Emilly', 'Cancelado', 'Vip'),
(110, 1, 'Stephany', 'Confirmado', 'Vip'),
(111, 1, 'Ana Lívia', 'Cancelado', 'Geral'),
(112, 1, 'Manuela', 'Pendente', 'Vip'),
(113, 1, 'Antônio', 'Confirmado', 'Vip'),
(114, 1, 'Benício', 'Confirmado', 'Vip'),
(115, 1, 'Josué', 'Confirmado', 'Vip'),
(116, 1, 'Mathias', 'Pendente', 'Vip'),
(117, 1, 'Luara', 'Confirmado', 'Geral'),
(118, 1, 'Davi Luiz', 'Pendente', 'Vip'),
(119, 1, 'Allana', 'Confirmado', 'Vip'),
(120, 1, 'Alana', 'Pendente', 'Geral'),
(121, 1, 'Vinícius', 'Confirmado', 'Vip'),
(122, 1, 'Otto', 'Cancelado', 'Geral'),
(123, 1, 'Juan', 'Pendente', 'Geral'),
(124, 1, 'Antonella', 'Confirmado', 'Geral'),
(125, 1, 'Guilherme', 'Cancelado', 'Geral'),
(126, 1, 'Maria Luiza', 'Confirmado', 'Geral'),
(127, 1, 'Rafael', 'Confirmado', 'Geral'),
(128, 1, 'Mariane', 'Confirmado', 'Vip'),
(129, 1, 'Luiza', 'Pendente', 'Vip'),
(130, 1, 'Catarina', 'Pendente', 'Geral');

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
(1, 'Casamento no Sítio', 'Fenda do biquine', '2026-01-17');

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
(1, 'Administrador', '75688329134', 'admin@wedding.com', '$2b$12$rjIYNwPQkyi3Okmv8ryJSeIW40OhM1m4dmut1DBq.RgAm2c3aNHvC', 'Admin'),
(2, 'Cerimonial', '6357729145', 'recepcao@wedding.com', '$2b$12$QRawXobe3BwC9p409p6IgO18/Di0X5zMt.chBbmLQZFO7HnzASbj2', 'Comum');

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
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_evento` (`id_evento`);

--
-- Índices de tabela `convidado`
--
ALTER TABLE `convidado`
  ADD PRIMARY KEY (`id_convidado`),
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
  MODIFY `id_area` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `checkin`
--
ALTER TABLE `checkin`
  MODIFY `id_checkin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `convidado`
--
ALTER TABLE `convidado`
  MODIFY `id_convidado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=131;

--
-- AUTO_INCREMENT de tabela `evento`
--
ALTER TABLE `evento`
  MODIFY `id_evento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `usuario_evento`
--
ALTER TABLE `usuario_evento`
  MODIFY `id_usuario_evento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
