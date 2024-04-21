from dotenv import load_dotenv
from flask import Flask, jsonify
from server_config import server_config

load_dotenv()
app = Flask(__name__)

db, migrate = server_config(app)

from routes import routes_blueprint

app.register_blueprint(routes_blueprint)


@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500


if __name__ == "__main__":
    app.run()
