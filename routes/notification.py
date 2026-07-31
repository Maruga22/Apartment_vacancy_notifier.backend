from flask import Blueprint

notification_bp = Blueprint(
    "notifications",
    __name__
)


@notification_bp.route("/subscribe")
def subscribe():

    return {
        "message": "Subscribe endpoint"
    }