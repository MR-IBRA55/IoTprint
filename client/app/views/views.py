from flask import Blueprint, render_template

website_bp = Blueprint("website", __name__)


@website_bp.route("/")
@website_bp.route("/home")
def home():
    return render_template("home.html")


@website_bp.route("/register")
def register():
    return render_template("register.html")


@website_bp.route("/login")
def login():
    return render_template("login.html")
