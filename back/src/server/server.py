from dotenv import load_dotenv
from flask import Flask, jsonify
from server_config import server_config


load_dotenv()
app = Flask(__name__)

db, migrate, jwt = server_config(app)

from routes import setup_routes

setup_routes(app)


@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500


if __name__ == "__main__":
    app.run()
