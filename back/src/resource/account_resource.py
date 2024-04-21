from flask import request, make_response, jsonify
from service.account_service import AccountService


class AccountResource:
    def __init__(self):
        self.account_service = AccountService()

    def register_account(self):
        register_form = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
            "password_confirm": request.form.get("passwordConfirm"),
        }
        account = self.account_service.register_account(**register_form)
        jsonify(account)

    def login(self):
        login_form = {
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }
        account = self.account_service.login(**login_form)

        if not account:
            return make_response("Credenciais inválidas", 401)

        return jsonify(account)
