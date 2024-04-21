from datetime import datetime
from server import db


class TeamModel(db.Model):
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    id_organization = db.Column(
        db.Integer, db.ForeignKey("organization.id"), nullable=False
    )
    id_account_creator = db.Column(
        db.Integer, db.ForeignKey("account.id"), nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime)

    organization = db.relationship("Organization", back_populates="team")
    account_creator = db.relationship("Account", back_populates="team")
