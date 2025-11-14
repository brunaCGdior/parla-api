import os
from flask import Flask, jsonify
from config import Config
from utils.db import init_db
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.activity_routes import activity_bp
from routes.character_routes import char_bp
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dao.token_dao import TokenDAO
from flask_cors import CORS   

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # CORS liberado
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    

    # Inicializa bcrypt e JWT
    Bcrypt(app)
    jwt = JWTManager(app)
    token_dao = TokenDAO()

    # Cria tabelas se não existirem
    init_db()

    # Registra rotas
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(activity_bp)
    app.register_blueprint(char_bp)

    # Bloqueio de token (logout)
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return token_dao.exists(jti)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "Token expired"}), 401

    # Rota raiz
    @app.route("/")
    def index():
        return jsonify({"message": "Parla API — running"})

    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
