# Importa o controlador IndexController do módulo src.controllers.controller
from src.controllers.controller import *

# Define as regras de rota e associa aos controladores correspondentes
routes = {
    'index_route': '/',                                  # Define a rota para o controlador do index
    'IndexController': IndexController.as_view('Index'), # Cria uma visão para o controlador de index
    
    'delete_route': '/delete/produto/<int:code>',        # Define a rota para o controlador de exclusão de produto, com um parâmetro de rota 'code'
    'DeleteController': DeleteProdutoController.as_view('Delete'), # Cria uma visão para o controlador de exclusão
    
    'update_route': '/update/produto/<int:code>',        # Define a rota para o controlador de atualização de produto, com um parâmetro de rota 'code'
    'UpdateController': UpdateProdutoController.as_view('Update'), # Cria uma visão para o controlador de atualização
    
    'categories_route': '/create/categorie',             # Define a rota para o controlador de categorias
    'CategoriesController': CategoriesController.as_view('Categories'), # Cria uma visão para o controlador de categorias
}
