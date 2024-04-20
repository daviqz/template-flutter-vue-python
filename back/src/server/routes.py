from flask import Blueprint, request
from resource.register_account_resource import register_account

routes = [
    {
        "endpoint": "/login",
        "methods": ["POST"],
        "function": register_account
    },
    {
        "endpoint": "/register",
        "methods": ["POST"],
        "function": register_account
    }
]

routes_blueprint = Blueprint('routes', __name__)

for route in routes:
    routes_blueprint.route(route["endpoint"], methods=route["methods"])(route["function"])