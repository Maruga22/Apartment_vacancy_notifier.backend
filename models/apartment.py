from database import db


class Apartment(db.Model):

    __tablename__ = "apartments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(100),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    bedrooms = db.Column(
        db.Integer,
        nullable=False
    )

    bathrooms = db.Column(
        db.Float,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "location": self.location,
            "price": self.price,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "description": self.description
        }