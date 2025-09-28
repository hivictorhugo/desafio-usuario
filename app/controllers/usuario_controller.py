from flask import Blueprint, request, jsonify
from app.services.usuario_service import (
    criar_usuario_service,
    listar_usuarios_service
)


usuario_bp = Blueprint('usuario', __name__)


@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    novo_usuario = criar_usuario_service(data)
    return jsonify({
        'id': novo_usuario.id,
        'nome': novo_usuario.nome,
        'email': novo_usuario.email
    }), 201
 

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = listar_usuarios_service()
    if not usuarios:
        return jsonify({"message": "Nenhum usuario encontrado."}), 200
    
    return jsonify([
        {
            "id": u.id,
            "nome": u.nome,
            "email": u.email
        } for u in usuarios
        
    ]), 200