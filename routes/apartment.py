from flask import Blueprint

apartment_bp = Blueprint(
    "apartments",
    __name__
)


@apartment_bp.route("/")
def get_apartments():

    return {
        "message": "Get Apartments"
    }


@apartment_bp.route("/add")
def add_apartment():

    return {
        "message": "Add Apartment"
    }