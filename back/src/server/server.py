from flask import Flask
from routes import routes_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run()