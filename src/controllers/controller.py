# Importa a classe MethodView do Flask e módulos necessários para a renderização de templates e manipulação de requisições
from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import pymysql  # Importa a biblioteca PyMySQL (presumo que src.db seja onde você tem a conexão com o banco de dados)

# Define um controlador de exemplo utilizando a classe MethodView do Flask
class IndexController(MethodView):
    def get(self):
        # Método para lidar com requisições GET
        # Retorna o conteúdo renderizado do template 'public/index.html'
        return render_template('public/index.html')

    def post(self):
        # Método para lidar com requisições POST
        # Obtém os dados do formulário enviado através da requisição POST
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']
        
        # Imprime os dados do formulário no console (pode ser útil para depuração)
        print(code, name, stock, value, category)
        
        # Retorna uma mensagem indicando que o produto foi cadastrado com sucesso
        return 'Produto Cadastrado com Sucesso!!'
