from datetime import datetime
from server import db


class OrganizationModel(db.Model):
    __tablename__ = "organization"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    id_product_type = db.Column(db.Integer, db.ForeignKey("product_type.id"))
    id_account_creator = db.Column(
        db.Integer, db.ForeignKey("account.id"), nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime)

    product_type = db.relationship("ProductType", back_populates="organization")
    account_creator = db.relationship("Account", back_populates="organization")
