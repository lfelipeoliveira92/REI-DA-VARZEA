from app import create_app

# Cria a instância do nosso aplicativo a partir da função que definimos no __init__.py
app = create_app()

if __name__ == "__main__":
    # Esta linha faz o servidor rodar localmente para testes
    # O 'host="0.0.0.0"' permite que ele seja acessível na sua rede
    app.run(host="0.0.0.0", port=5000, debug=True)
