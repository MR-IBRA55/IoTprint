from flask import Blueprint, render_template

website_bp = Blueprint("website", __name__)


@website_bp.route("/")
@website_bp.route("/home")
def home():
    return render_template("index.html")
