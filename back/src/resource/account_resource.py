from flask import request
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
        return self.account_service.register_account(**register_form)
