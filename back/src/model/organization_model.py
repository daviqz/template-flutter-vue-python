from server import db
from model.association.account_organization_model_association import (
    AccountOrganizationModelAssociation,
)


class OrganizationModel(db.Model):
    __tablename__ = "organization"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    id_product_type = db.Column(db.Integer, db.ForeignKey("product_type.id"))
    id_account_creator = db.Column(
        db.Integer, db.ForeignKey("account.id"), nullable=False
    )
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.sql.func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.sql.func.now(),
        onupdate=db.sql.func.now(),
    )
    deleted_at = db.Column(db.DateTime(timezone=True))

    product_type = db.relationship("ProductTypeModel")
    account_creator = db.relationship("AccountModel")
    accounts = db.relationship(
        "AccountModel",
        secondary=AccountOrganizationModelAssociation,
        back_populates="organizations",
    )
    teams = db.relationship("TeamModel", back_populates="organization")
