from server.extensions import db

account_organization_table_association = db.Table(
    "account_organization",
    db.metadata,
    db.Column("account_id", db.ForeignKey("account.id")),
    db.Column("organization_id", db.ForeignKey("organization.id")),
)
