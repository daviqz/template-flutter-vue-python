from flask import Blueprint
from resource.account_resource import AccountResource

account_resource = AccountResource()

routes = [
    {
        "endpoint": "/login",
        "methods": ["POST"],
        "function": account_resource.register_account,
    },
    {
        "endpoint": "/register",
        "methods": ["POST"],
        "function": account_resource.register_account,
    },
]

routes_blueprint = Blueprint("routes", __name__)

for route in routes:
    routes_blueprint.route(route["endpoint"], methods=route["methods"])(
        route["function"]
    )
