from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from utils.account_utils import validate_fields_register_account, validate_fields_login
from repository.account_repository import AccountRepository
from dto.account_dto import AccountDTO


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
        account_model = self.account_repository.register_account(
            username, email, hashed_password
        )
        account_dto = AccountDTO.from_model(account_model)
        return account_dto.to_dictionary()

    def login(self, email, password):
        field_validate = validate_fields_login(email, password)

        if not field_validate["is_valid"]:
            return field_validate

        account_found = self.account_repository.get_account_by_email(email)

        if account_found:
            if check_password_hash(account_found.password, password):
                access_token = create_access_token(identity=email)
                account_dto = AccountDTO.from_model(account_found)
                return {
                    "access_token": access_token,
                    "account": account_dto.to_dictionary(),
                }
        return None

    def get_own_account_by_email(self, email):
        account_found = self.account_repository.get_account_by_email(email)
        account_dto = AccountDTO.from_model(account_found)
        return account_dto.to_dictionary()
