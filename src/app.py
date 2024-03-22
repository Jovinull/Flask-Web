# Importa a classe Flask do módulo flask
from flask import Flask

# Importa as rotas definidas no arquivo routes.py
from src.routes.routes import *

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração da chave secreta para proteção contra ataques CSRF
app.config.from_mapping(
    SECRET_KEY = 'development'
)

# Adiciona as regras de URL definidas no arquivo routes.py

# Mapeia a rota definida em 'index_route' para o controlador 'IndexController'
app.add_url_rule(routes['index_route'], view_func=routes['IndexController'])

# Mapeia a rota definida em 'delete_route' para o controlador 'DeleteProdutoController'
app.add_url_rule(routes['delete_route'], view_func=routes['DeleteController'])

# Mapeia a rota definida em 'update_route' para o controlador 'UpdateProdutoController'
app.add_url_rule(routes['update_route'], view_func=routes['UpdateController'])

# Mapeia a rota definida em 'categories_route' para o controlador 'CategoriesController'
app.add_url_rule(routes['categories_route'], view_func=routes['CategoriesController'])
