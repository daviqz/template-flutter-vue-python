from flask import Flask, jsonify
import sys
from dotenv import load_dotenv
from waitress import serve
from loguru import logger
from server.server_config import server_config
from server.extensions import db, migrate
from server.routes import setup_routes
import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv()
app = Flask(__name__)

app, jwt = server_config(app)


db.init_app(app)
db.configure_mappers()

migrate.init_app(app, db)


setup_routes(app)


@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500


logger.remove(0)
logger.add(
    sys.stderr,
    format="<yellow>{time:YYYY-MM-DD HH:mm:ss} | {message}</yellow>",
    level="DEBUG",
)
logger.debug("#################################################################")
logger.debug("Servidor iniciado com sucesso! Escutando em http://localhost:8080")
logger.debug("#################################################################")

if __name__ == "__main__":
    serve(app, listen="*:8080")
