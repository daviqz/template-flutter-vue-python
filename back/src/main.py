from dotenv import load_dotenv
from flask import Flask, jsonify
from server.server_config import server_config
from waitress import serve
from server.extensions import db, migrate
from server.routes import setup_routes

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")

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


if __name__ == "__main__":
    serve(app, listen="*:8080")
