from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from repository.account_repository import AccountRepository
from utils.account_utils import validate_fields_register_account, validate_fields_login


class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

    def register_account(self, username, email, password, password_confirm):
        field_validate = validate_fields_register_account(
            username, email, password, password_confirm
        )

        if not field_validate["is_valid"]:
            return field_validate

        hashed_password = generate_password_hash(password)
        return self.account_repository.register_account(
            username, email, hashed_password
        )

    def login(self, email, password):
        field_validate = validate_fields_login(email, password)

        if not field_validate["is_valid"]:
            return field_validate

        account_found = self.account_repository.get_account_by_email(email)

        if account_found:
            if check_password_hash(account_found.password, password):
                access_token = create_access_token(identity=email)
                return access_token
        return None
