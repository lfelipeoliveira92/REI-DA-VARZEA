from flask import Flask

def create_app():
    """
    Função que cria e configura a instância do nosso aplicativo Flask.
    """
    app = Flask(__name__)

    # --- Configurações Futuras ---
    # Aqui entrará a conexão com o banco de dados e o registro das nossas rotas (API).

    # Uma rota de teste para garantir que o servidor está no ar
    @app.route("/")
    def index():
        return "<h1>O motor do Rei da Várzea está no ar!</h1>"

    return app
