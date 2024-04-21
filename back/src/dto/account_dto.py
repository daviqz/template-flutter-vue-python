class AccountDTO:
    def __init__(self, id, username, email, created_at, updated_at, deleted_at):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def to_dictionary(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }

    @classmethod
    def from_model(cls, account_model):
        return cls(
            id=account_model.id,
            username=account_model.username,
            email=account_model.email,
            created_at=account_model.created_at,
            updated_at=account_model.updated_at,
            deleted_at=account_model.deleted_at,
        )
