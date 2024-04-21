from server import db


class AccountTeamAccountTypeModelAssociation(db.Model):
    __tablename__ = "account_team_account_type"

    id_account = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    id_account_type = db.Column(
        db.Integer, db.ForeignKey("account_type.id"), nullable=False
    )

    __table_args__ = (db.PrimaryKeyConstraint("id_account", "id_account_type"),)
