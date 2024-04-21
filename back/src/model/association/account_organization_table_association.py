from server import db

account_organization_table_association = db.Table(
    "account_organization",
    db.metadata,
    db.Column("account_id", db.ForeignKey("account.id")),
    db.Column("organization_id", db.ForeignKey("organization.id")),
)

# class AccountOrganizationModelAssociation(db.Model):
#     __tablename__ = "account_organization"

#     id_account = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
#     id_organization = db.Column(
#         db.Integer, db.ForeignKey("organization.id"), nullable=False
#     )

#     __table_args__ = (db.PrimaryKeyConstraint("id_account", "id_organization"),)
