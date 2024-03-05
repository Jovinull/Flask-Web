from flask import Flask
from src.routes.routes import *

# Inicializa a aplicação Flask
app = Flask(__name__)

# Adiciona as regras de URL definidas no arquivo routes.py
# Mapeia a rota definida em 'test_controller_route' para o controlador 'test_controller'
app.add_url_rule(routes['index_route'], view_func=routes['IndexController'])

app.register_error_handler(routes['not_found_route'], routes['not_found_controller'])
