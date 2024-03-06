# Importa a classe MethodView do Flask e módulos necessários para a renderização de templates e manipulação de requisições
from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql  # Importa a biblioteca PyMySQL (presumo que src.db seja onde você tem a conexão com o banco de dados)

# Define um controlador de exemplo utilizando a classe MethodView do Flask
class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM produtos')
            data = cur.fetchall()
        # Método para lidar com requisições GET
        # Retorna o conteúdo renderizado do template 'public/index.html'
        return render_template('public/index.html', data=data)

    def post(self):
        # Método para lidar com requisições POST
        # Obtém os dados do formulário enviado através da requisição POST
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        # category = request.form['category']
        
        with mysql.cursor() as cur:
            cur.execute('INSERT INTO produtos(code, name, stock, value) VALUES(%s, %s, %s, %s)', (code, name, stock, value))
            cur.connection.commit()
            return redirect('/')

class DeleteProdutoController(MethodView):
    def post(self, code):
        with mysql.cursor() as cur:
            cur.execute('DELETE FROM produtos WHERE code=%s', (code,))
            cur.connection.commit()
            return redirect('/')

class UpdateProdutoController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM produtos WHERE code=%s', (code,))
            produto = cur.fetchone()
            return render_template('public/update.html', produto=produto)

    def post(self, code):
        produtoCode = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
