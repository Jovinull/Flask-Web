# Importa a classe Flask do módulo flask
from flask import Flask
from src.routes.routes import *

# Inicializa a aplicação Flask
app = Flask(__name__)

# Adiciona as regras de URL definidas no arquivo routes.py
# Mapeia a rota definida em 'index_route' para o controlador 'IndexController'
app.add_url_rule(routes['index_route'], view_func=routes['IndexController'])

app.add_url_rule(routes['delete_route'], view_func=routes['DeleteController'])

app.add_url_rule(routes['update_route'], view_func=routes['UpdateController'])

app.add_url_rule(routes['categories_route'], view_func=routes['CategoriesController'])
