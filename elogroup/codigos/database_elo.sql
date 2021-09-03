CREATE DATABASE database_elo;
USE database_elo;

CREATE TABLE DIM_Produto (
    ID_produto INTEGER AUTO_INCREMENT PRIMARY KEY,
    Cod_produto INTEGER NOT NULL,
    Nm_produto VARCHAR(255) NOT NULL,
    Secao VARCHAR(255) NOT NULL,
    Grupo VARCHAR(255) NOT NULL,
    Subgrupo VARCHAR(255) NOT NULL
);

CREATE TABLE DIM_Tempo (
    ID_tempo INTEGER AUTO_INCREMENT PRIMARY KEY,
    Ano INTEGER NOT NULL,
    Mes INTEGER NOT NULL,
    Dia INTEGER NOT NULL,
    num_data INTEGER NOT NULL
);

CREATE TABLE DIM_Loja (
    ID_loja INTEGER AUTO_INCREMENT PRIMARY KEY,
    Cod_loja INTEGER NOT NULL,
    Nm_loja VARCHAR(255) NOT NULL
);

CREATE TABLE DIM_Cliente (
    ID_cliente INTEGER AUTO_INCREMENT PRIMARY KEY,
    Estado_civil VARCHAR(255) NOT NULL,
    Sexo VARCHAR(255) NOT NULL,
    Bairro VARCHAR(255) NOT NULL
);

CREATE TABLE FT_Vendas (
    vendas_produto INTEGER NOT NULL,
    vendas_loja INTEGER NOT NULL,
    vendas_cliente INTEGER NOT NULL,
    vendas_tempo INTEGER NOT NULL,
    Qtde_vendida INTEGER NOT NULL,
    Receita_venda DECIMAL NOT NULL,
    FOREIGN KEY(vendas_produto) REFERENCES DIM_Produto(ID_produto),
    FOREIGN KEY(vendas_loja) REFERENCES DIM_Loja(ID_loja),
    FOREIGN KEY(vendas_cliente) REFERENCES DIM_Cliente(ID_cliente),
    FOREIGN KEY(vendas_tempo) REFERENCES DIM_Tempo(ID_tempo)
);