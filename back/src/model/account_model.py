from datetime import datetime
from server import db


class AccountModel(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    id_account_view_type = db.Column(db.Integer, db.ForeignKey("account_type.id"))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime)

    account_view_type = db.relationship("AccountType", back_populates="account")

    def __init__(self, username, email, password, id_account_type=None):
        self.username = username
        self.email = email
        self.password = password
        self.id_account_type = id_account_type
