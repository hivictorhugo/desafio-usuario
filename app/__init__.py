from flask import Flask
from app.extensions import db, migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)

from app.models.usuario_model import Usuario

#with app.app_context():
#    db.create_all()


from app.controllers.usuario_controller import usuario_bp
app.register_blueprint(usuario_bp)


@app.route('/')
def home():
    return "API funcionando"

if __name__ == "__main__":
    app.run(debug=True)


