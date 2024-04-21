from server import db


class AccountOrganizationModel(db.Model):
    __tablename__ = "account_organization"

    id_account = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    id_organization = db.Column(
        db.Integer, db.ForeignKey("organization.id"), nullable=False
    )

    __table_args__ = (db.PrimaryKeyConstraint("id_account", "id_organization"),)
