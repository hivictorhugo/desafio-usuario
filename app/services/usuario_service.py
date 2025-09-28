from app.extensions import db
from app.models.usuario_model import Usuario


def criar_usuario_service(data):
    novo = Usuario(**data)
    db.session.add(novo)
    db.session.commit()
    return novo

def listar_usuarios_service():
    return Usuario.query.all()


    
