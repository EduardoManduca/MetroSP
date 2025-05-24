-- Projeto: Simulação de Metrô para Maquinistas
-- Objetivo: Estruturar o banco de dados para permitir cadastro de usuários (maquinistas e supervisores), 
-- registro de simulações, histórico de resultados e recomendações automáticas.

-- 1) Criação do schema
CREATE DATABASE IF NOT EXISTS `metro_simulacao`
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
USE `metro_simulacao`;

-- 2) Tabela de Usuários
-- Credenciais maquinista e supervisor
CREATE TABLE `Usuario` (
  `idUsuario`   INT          NOT NULL AUTO_INCREMENT COMMENT 'Identificador único do usuário',
  `Senha`       CHAR(60)     NOT NULL COMMENT 'Senha criptografada do usuário',
  `Email`       VARCHAR(100) NOT NULL COMMENT 'Email único para login',
  `Tipo`        ENUM('maquinista','supervisor') NOT NULL COMMENT 'Perfil de acesso',
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `UQ_Usuario_Email` (`Email`)
) ENGINE=InnoDB;

-- 3) Tabela de Histórico
-- Armazena estatísticas agregadas de performance de cada maquinista.
CREATE TABLE `Historico` (
  `idUsuario`       INT       NOT NULL COMMENT 'Identificador único do usuário',
  `Acertos`         SMALLINT  NOT NULL COMMENT 'Total de acertos em todas as simulações',
  `NumSimulacoes`   SMALLINT  NOT NULL COMMENT 'Quantidade de vezes que o usuário iniciou uma simulação',
  `MediaPontuacoes` INT       NOT NULL COMMENT 'Média das pontuações obtidas',
  `TotalPontos`     INT       NOT NULL COMMENT 'Soma de todos os pontos ganhos',
  PRIMARY KEY (`idUsuario`),
  CONSTRAINT `FK_Historico_Usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `Usuario`(`idUsuario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 4) Tabela de Simulações
-- Cada registro representa uma sessão de treino ou avaliação.
CREATE TABLE `Simulacao` (
  `idSimulacao`     INT       NOT NULL AUTO_INCREMENT COMMENT 'Identificador único da simulação',
  `idUsuario`       INT       NOT NULL COMMENT 'Identificador do usuário que realizou a simulação',
  `pontuacao_total` INT       NOT NULL COMMENT 'Pontuação obtida na simulação',
  `num_acertos`     SMALLINT  NOT NULL COMMENT 'Número de procedimentos corretos durante a simulação',
  PRIMARY KEY (`idSimulacao`),
  KEY `FK_Simulacao_Usuario` (`idUsuario`),
  CONSTRAINT `FK_Simulacao_Usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `Usuario`(`idUsuario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 5) Tabela de Recomendações
-- Feedback gerado para cada simulação, sugerindo correções ou próximos passos.
CREATE TABLE `Recomendacao` (
  `idSimulacao`   INT          NOT NULL COMMENT 'Identificador da simulação associada',
  `Erro`          VARCHAR(100) NOT NULL COMMENT 'Descrição resumida do principal erro identificado',
  `Recomendacao`  TEXT         NOT NULL COMMENT 'Orientação ou dica para melhorar no próximo treino',
  PRIMARY KEY (`idSimulacao`),
  CONSTRAINT `FK_Recomendacao_Simulacao`
    FOREIGN KEY (`idSimulacao`)
    REFERENCES `Simulacao`(`idSimulacao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;
