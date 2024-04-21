from server import db


class MembershipModel(db.Model):
    __tablename__ = "membership"

    id = db.Column(db.Integer, primary_key=True)
    id_account = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    id_team = db.Column(db.Integer, db.ForeignKey("team.id"), nullable=False)
    id_account_type = db.Column(
        db.Integer, db.ForeignKey("account_type.id"), nullable=False
    )
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.sql.func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.sql.func.now(),
        onupdate=db.sql.func.now(),
    )
    deleted_at = db.Column(db.DateTime(timezone=True))

    team = db.relationship("Team", back_populates="memberships")
    account_type = db.relationship("AccountTypeModel")
    account = db.relationship("AccountModel")

    def __init__(self, id_account, id_team, id_account_type):
        self.id_account = id_account
        self.team_id = id_team
        self.id_account_type = id_account_type
