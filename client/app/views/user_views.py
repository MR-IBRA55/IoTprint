from flask import Blueprint, render_template

user_bp = Blueprint("user", __name__)


@user_bp.route("/profile")
def profile():
    return render_template("profile.html")


@user_bp.route("/upload")
def upload():
    return render_template("upload_file.html")


@user_bp.route("/my_files")
def my_files():
    return render_template("my_files.html")


@user_bp.route("/orders")
def orders():
    return render_template("orders.html")


@user_bp.route("/logout")
def logout():
    return render_template("logout.html")
