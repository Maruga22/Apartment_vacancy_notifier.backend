from database import db
from datetime import datetime


class Apartment(db.Model):
    __tablename__ = "apartments"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    location = db.Column(db.String(255), nullable=False)

    price = db.Column(db.Float, nullable=False)

    bedrooms = db.Column(db.Integer, nullable=False)

    bathrooms = db.Column(db.Integer, nullable=False)

    description = db.Column(db.Text, nullable=False)

    image = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "location": self.location,
            "price": self.price,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "description": self.description,
            "image": self.image,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M")
            if self.created_at
            else None,
        }