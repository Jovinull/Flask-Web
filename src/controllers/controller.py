from flask.views import MethodView

# Define um controlador de exemplo utilizando a classe MethodView do Flask
class TestController(MethodView):
    def get(self):
        # Método para lidar com requisições GET
        return 'Teste Controller'
