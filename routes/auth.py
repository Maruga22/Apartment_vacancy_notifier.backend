from flask import Blueprint, request, jsonify
from database import db
from models.user import User
import bcrypt

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")

    if not all([name, email, password]):
        return jsonify({"message": "All required fields are required"}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"message": "Email already exists"}), 409

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    new_user = User(
        name=name,
        email=email,
        phone=phone,
        password=hashed_password.decode("utf-8")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Registration successful",
        "user": new_user.to_dict()
    }), 201

@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    print("Received:", data)  # Debugging line

    email = data.get("email")
    password = data.get("password")

    # Check if all fields are provided
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Find user by email
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    # Compare entered password with hashed password
    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user.password.encode("utf-8")
    ):
        return jsonify({"message": "Invalid email or password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": user.to_dict()
    }), 200