from src.controllers.controller import *

# Define as regras de rota e associa aos controladores correspondentes
routes = {
    'index_route': '/',  # Rota para o controlador do index
    'IndexController': IndexController.as_view('Index'),  # Cria uma visão para o controlador de index
}
