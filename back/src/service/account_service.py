from repository.account_repository import AccountRepository
from utils.account_utils import validate_fields_register_account


class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

    def register_account(self, username, email, password, password_confirm):
        field_validate = validate_fields_register_account(
            username, email, password, password_confirm
        )
        if not field_validate["is_valid"]:
            return field_validate

        return self.account_repository.register_account(username, email, password)
