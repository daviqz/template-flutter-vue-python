from server import db
from model.association.account_organization_table_association import (
    account_organization_table_association,
)


class AccountModel(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    id_account_view_type = db.Column(db.Integer, db.ForeignKey("account_type.id"))
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.sql.func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.sql.func.now(),
        onupdate=db.sql.func.now(),
    )
    deleted_at = db.Column(db.DateTime(timezone=True))

    account_view_type = db.relationship("AccountTypeModel")
    organizations = db.relationship(
        "OrganizationModel",
        secondary=account_organization_table_association,
        back_populates="accounts",
    )
    memberships = db.relationship(
        "MembershipModel",
        back_populates="account",
    )

    def __init__(self, username, email, password, id_account_view_type=None):
        self.username = username
        self.email = email
        self.password = password
        self.id_account_view_type = id_account_view_type
