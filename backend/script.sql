CREATE DATABASE IF NOT EXISTS anunbis;
use anunbis;

CREATE TABLE IF NOT EXISTS professores(
codigo int(100) AUTO_INCREMENT,
nome varchar(30) NOT NULL,
email varchar(50),
PRIMARY KEY (codigo)
);