from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from .api.brands import get_brands

# from flaskr.auth import login_required

bp = Blueprint("brands", __name__)


@bp.route("/")
def index():
    brands = get_brands().json()["brands"]
    return render_template("brands/index.html", brands=brands)
