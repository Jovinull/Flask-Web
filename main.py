from src.app import app

# Configurações para execução da aplicação
HOST = 'localhost'
PORT = 4000
DEBUG = True

# Verifica se o script está sendo executado diretamente
if (__name__ == '__main__'):
    # Inicia a aplicação Flask
    app.run(HOST, PORT, DEBUG)
