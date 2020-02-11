from flask import Blueprint, render_template, url_for

website_bp = Blueprint('website', __name__,  template_folder='templates')


@website_bp.route('/')
def home():
    return render_template("index.html")
