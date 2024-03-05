from src.controllers.errors import NotFoundController
from src.controllers.controller import *

# Define as regras de rota e associa aos controladores correspondentes
routes = {
    'index_route': '/',  # Rota para o controlador de teste
    'IndexController': IndexController.as_view('Index'),  # Cria uma visão para o controlador de teste
    'not_found_route': 404,
    'not_found_controller': NotFoundController.as_view('not_found'),
}
