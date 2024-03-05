-- Cria a tabela 'produtos' se ela não existir
CREATE TABLE IF NOT EXISTS produtos (
    code INT(4) UNSIGNED ZEROFILL NOT NULL, -- Código do produto (inteiro sem sinal com preenchimento de zeros)
    name CHAR(50),                          -- Nome do produto (cadeia de caracteres com tamanho máximo de 50)
    stock INT NOT NULL,                     -- Quantidade disponível em estoque (inteiro não nulo)
    value FLOAT,                            -- Valor do produto (número de ponto flutuante)
    id_category tinyint NULL,               -- Chave estrangeira referenciando a tabela 'categories'
    PRIMARY KEY ('code')                    -- Define a chave primária na coluna 'code'
);

-- Cria a tabela 'categories' se ela não existir
CREATE TABLE IF NOT EXISTS categories (
    id tinyint NOT NULL,                  -- Identificador da categoria (inteiro pequeno não nulo)
    name CHAR(40) NOT NULL,               -- Nome da categoria (cadeia de caracteres com tamanho máximo de 40)
    description VARCHAR(200),             -- Descrição da categoria (cadeia de caracteres com tamanho máximo de 200)
    PRIMARY KEY ('id')                    -- Define a chave primária na coluna 'id'
);

-- Adiciona uma chave estrangeira à tabela 'produtos' referenciando a tabela 'categories'
ALTER TABLE produtos ADD FOREIGN KEY ('id_category') REFERENCES categories ('id');
