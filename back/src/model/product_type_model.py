from server.extensions import db


class ProductTypeModel(db.Model):
    __tablename__ = "product_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.sql.func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.sql.func.now(),
        onupdate=db.sql.func.now(),
    )
    deleted_at = db.Column(db.DateTime(timezone=True))
