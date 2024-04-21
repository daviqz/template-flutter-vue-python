from flask import Blueprint
from flask_jwt_extended import jwt_required
from resource.account_resource import AccountResource

account_resource = AccountResource()

routes = [
    {
        "endpoint": "/login",
        "methods": ["POST"],
        "function": account_resource.login,
        "is_private": False,
    },
    {
        "endpoint": "/register",
        "methods": ["POST"],
        "function": account_resource.register_account,
        "is_private": False,
    },
]

routes_blueprint = Blueprint("routes", __name__)

for route in routes:
    endpoint = route["endpoint"]
    methods = route["methods"]
    function = route["function"]

    decorated_function = function
    if route["is_private"]:
        decorated_function = jwt_required()(function)

    routes_blueprint.route(endpoint, methods=methods)(decorated_function)
