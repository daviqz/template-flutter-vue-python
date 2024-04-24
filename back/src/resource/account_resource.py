from flask import request, make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from service.account_service import AccountService


class AccountResource:
    def __init__(self):
        self.account_service = AccountService()

    def login(self):
        login_form = {
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }
        account_auth = self.account_service.login(**login_form)

        if not account_auth:
            return make_response("Credenciais inválidas", 401)

        return jsonify(account_auth)

    def register_account(self):
        register_form = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
            "password_confirm": request.form.get("passwordConfirm"),
        }
        account = self.account_service.register_account(**register_form)
        return jsonify(account)

    def get_own_account_by_email(self):
        current_user_email = get_jwt_identity()
        account = self.account_service.get_own_account_by_email(current_user_email)
        return jsonify(account)
