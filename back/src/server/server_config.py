import os

# import sys
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from loguru import logger

logger.debug("That's it, beautiful and simple logging!")


def server_config(app):
    # cors
    CORS(app)

    # jwt
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)

    # database config
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return app, jwt
