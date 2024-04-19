from flask import Blueprint

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route("/login", methods=['POST'])
def hello_world():
    return 'Hello, World!'