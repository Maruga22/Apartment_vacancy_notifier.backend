from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from database import db
from models.apartment import Apartment
import os
import uuid

apartment_bp = Blueprint("apartments", __name__)

# Folder where uploaded images will be stored
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ===========================
# CREATE APARTMENT
# ===========================
@apartment_bp.route("/", methods=["POST"])
def create_apartment():

    title = request.form.get("title")
    location = request.form.get("location")
    price = request.form.get("price")
    bedrooms = request.form.get("bedrooms")
    bathrooms = request.form.get("bathrooms")
    description = request.form.get("description")

    image = request.files.get("image")

    image_filename = ""

    if image and image.filename != "":
        extension = os.path.splitext(image.filename)[1]
        image_filename = f"{uuid.uuid4()}{extension}"

        image.save(
            os.path.join(
                UPLOAD_FOLDER,
                secure_filename(image_filename)
            )
        )

    apartment = Apartment(
        title=title,
        location=location,
        price=float(price),
        bedrooms=int(bedrooms),
        bathrooms=int(bathrooms),
        description=description,
        image=image_filename,
        user_id=data["user_id"]
    )

    db.session.add(apartment)
    db.session.commit()

    return jsonify({
        "message": "Apartment posted successfully",
        "apartment": apartment.to_dict()
    }), 201


# ===========================
# GET ALL APARTMENTS
# ===========================
@apartment_bp.route("/", methods=["GET"])
def get_apartments():

    apartments = Apartment.query.order_by(
        Apartment.created_at.desc()
    ).all()

    apartment_list = []

    for apartment in apartments:

        apartment_list.append({
            "id": apartment.id,
            "title": apartment.title,
            "location": apartment.location,
            "price": apartment.price,
            "bedrooms": apartment.bedrooms,
            "bathrooms": apartment.bathrooms,
            "description": apartment.description,
            "image": apartment.image,
            "created_at": apartment.created_at
        })

    return jsonify(apartment_list)


# ===========================
# GET ONE APARTMENT
# ===========================
@apartment_bp.route("/<int:id>", methods=["GET"])
def get_apartment(id):

    apartment = Apartment.query.get_or_404(id)

    return jsonify(apartment.to_dict())


# ===========================
# UPDATE APARTMENT
# ===========================
@apartment_bp.route("/<int:id>", methods=["PUT"])
def update_apartment(id):

    apartment = Apartment.query.get_or_404(id)

    apartment.title = request.form.get("title")
    apartment.location = request.form.get("location")
    apartment.price = float(request.form.get("price"))
    apartment.bedrooms = int(request.form.get("bedrooms"))
    apartment.bathrooms = int(request.form.get("bathrooms"))
    apartment.description = request.form.get("description")

    image = request.files.get("image")

    if image and image.filename != "":

        # Delete old image
        if apartment.image:

            old_image = os.path.join(
                UPLOAD_FOLDER,
                apartment.image
            )

            if os.path.exists(old_image):
                os.remove(old_image)

        extension = os.path.splitext(image.filename)[1]

        filename = f"{uuid.uuid4()}{extension}"

        image.save(
            os.path.join(
                UPLOAD_FOLDER,
                secure_filename(filename)
            )
        )

        apartment.image = filename

    db.session.commit()

    return jsonify({
        "message": "Apartment updated successfully",
        "apartment": apartment.to_dict()
    })


# ===========================
# DELETE APARTMENT
# ===========================
@apartment_bp.route("/<int:id>", methods=["DELETE"])
def delete_apartment(id):

    apartment = Apartment.query.get_or_404(id)

    if apartment.image:

        image_path = os.path.join(
            UPLOAD_FOLDER,
            apartment.image
        )

        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(apartment)
    db.session.commit()

    return jsonify({
        "message": "Apartment deleted successfully"
    })