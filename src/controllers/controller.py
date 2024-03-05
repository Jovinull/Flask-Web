from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import pymysql

# Define um controlador de exemplo utilizando a classe MethodView do Flask
class IndexController(MethodView):
    def get(self):
        # Método para lidar com requisições GET
        return 'Teste Controller'

    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']
