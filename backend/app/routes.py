from flask import Blueprint, request, jsonify

# Cria um "roteador" para organizar os endpoints
# Todos os endpoints que projetamos (login, cadastro, etc.) serão adicionados aqui.
api = Blueprint('api', __name__)

@api.route("/test")
def test_route():
    """Uma rota de teste para garantir que o arquivo foi carregado."""
    return jsonify({"message": "As rotas da API estão funcionando!"})

# Exemplo de como um endpoint real ficaria aqui:
# @api.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     # ... lógica de cadastro ...
#     return jsonify({"message": "Usuário registrado!"}), 201
