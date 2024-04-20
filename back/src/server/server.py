from dotenv import load_dotenv
from server_config import server_config
load_dotenv()
server_config()

from flask import Flask
from flask_cors import CORS
from routes import routes_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run()