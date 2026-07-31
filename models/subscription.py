from database import db


class Subscription(db.Model):

    __tablename__ = "subscriptions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(120),
        nullable=False
    )

    location = db.Column(
        db.String(100),
        nullable=False
    )

    max_price = db.Column(
        db.Float,
        nullable=False
    )

    min_bedrooms = db.Column(
        db.Integer,
        default=1
    )

    def to_dict(self):

        return {
            "id": self.id,
            "email": self.email,
            "location": self.location,
            "max_price": self.max_price,
            "min_bedrooms": self.min_bedrooms
        }