# Importa o controlador IndexController do módulo src.controllers.controller
from src.controllers.controller import *

# Define as regras de rota e associa aos controladores correspondentes
routes = {
    'index_route': '/',                                  # Rota para o controlador do index
    'IndexController': IndexController.as_view('Index'), # Cria uma visão para o controlador de index
    
    'delete_route': '/delete/produto/<int:code>',
    'DeleteController': DeleteProdutoController.as_view('Delete'),
    
    'update_route': '/update/produto/<int:code>',
    'UpdateController': UpdateProdutoController.as_view('Update'),
    
    'categories_route': '/create/categorie',
    'CategoriesController': CategoriesController.as_view('Categories'),
}
