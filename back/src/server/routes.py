from resource.account_resource import AccountResource


def setup_routes(app):
    account_resource = AccountResource()

    @app.route("/account/login", methods=["POST"])
    def _login():
        return account_resource.login()

    @app.route("/account/register", methods=["POST"])
    def _register_account():
        return account_resource.register_account()
