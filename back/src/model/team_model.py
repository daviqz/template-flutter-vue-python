from datetime import datetime
from server.extensions import db


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
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    deleted_at = db.Column(db.DateTime(timezone=True))

    organization = db.relationship("OrganizationModel", back_populates="teams")
    memberships = db.relationship("MembershipModel", back_populates="team")
    account_creator = db.relationship("AccountModel")
