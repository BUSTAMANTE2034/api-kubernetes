from flask import Flask
from .config import Config  
from .models import db  
from .services import api  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar el blueprint
    app.register_blueprint(api, url_prefix='/api')

    return app
