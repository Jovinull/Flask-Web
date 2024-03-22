# Projeto Flask Web

Este é um projeto Flask para uma aplicação web de gerenciamento de produtos e categorias.

## Estrutura do Banco de Dados

O projeto utiliza um banco de dados MySQL com as seguintes tabelas:

### Tabela `produtos`

- `code`: Código do produto (inteiro sem sinal com preenchimento de zeros)
- `name`: Nome do produto (cadeia de caracteres com tamanho máximo de 50)
- `stock`: Quantidade disponível em estoque (inteiro não nulo)
- `value`: Valor do produto (número de ponto flutuante)
- `id_category`: Chave estrangeira referenciando a tabela 'categories'
- Chave primária: `code`

### Tabela `categories`

- `id`: Identificador da categoria (inteiro pequeno não nulo)
- `name`: Nome da categoria (cadeia de caracteres com tamanho máximo de 40)
- `description`: Descrição da categoria (cadeia de caracteres com tamanho máximo de 200)
- Chave primária: `id`

## Dependências do Projeto

Além do Flask, o projeto utiliza as seguintes dependências Python:

```
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
greenlet==3.0.3
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
PyMySQL==1.1.0
typing_extensions==4.10.0
Werkzeug==3.0.1
```

## Como Executar o Projeto

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python e o MySQL instalados em sua máquina.
3. Instale as dependências Python listadas acima.
4. Importe o arquivo `db.sql` para criar o esquema do banco de dados.
5. Execute a aplicação Flask executando o arquivo `app.py`.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
