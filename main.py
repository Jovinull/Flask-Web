# Importa a instância 'app' da aplicação Flask do módulo src.app
from src.app import app

# Configurações para execução da aplicação
HOST = 'localhost'  # Endereço do servidor
PORT = 4000         # Porta em que a aplicação será executada
DEBUG = True        # Modo de depuração (True para ativar, False para desativar)

# Verifica se o script está sendo executado diretamente
if (__name__ == '__main__'):
    # Inicia a aplicação Flask
    app.run(HOST, PORT, DEBUG)
