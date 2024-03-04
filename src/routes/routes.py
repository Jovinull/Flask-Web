from src.controllers.controller import *

# Define as regras de rota e associa aos controladores correspondentes
routes = {
    'test_controller_route': '/',  # Rota para o controlador de teste
    'test_controller': TestController.as_view('test'),  # Cria uma visão para o controlador de teste
}
