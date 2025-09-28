from app.extensions import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    #senha = db.Column(db.String(), nullable=False)

#    def __repr__(self):
#        return f'<Usuario {self.nome}>'