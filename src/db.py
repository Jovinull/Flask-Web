# Importa a biblioteca PyMySQL para interagir com o MySQL
import pymysql

# Estabelece uma conexão com o banco de dados MySQL
# Substitua os valores apropriados para 'host', 'user', 'password' e 'database'
# Nota: O campo 'password' está vazio ('') neste exemplo; você deve fornecer sua senha MySQL
mysql = pymysql.connect(
    host='localhost',    # Endereço do servidor MySQL
    port=3306,           # Porta padrão para o MySQL
    user='root',         # Nome de usuário para acessar o MySQL
    password='',         # Senha para acessar o MySQL (substitua com sua senha)
    database='db_flask'  # Nome do banco de dados que você deseja acessar
)

# A conexão está agora estabelecida e armazenada na variável 'mysql'
# Você pode usar esta conexão para realizar operações no banco de dados MySQL
