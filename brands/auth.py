import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from .api.user import post_login, post_signup
from jose import jwt
from dotenv import dotenv_values


bp = Blueprint("auth", __name__, url_prefix="/auth")

config = dotenv_values(".env")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        return redirect(url_for("auth.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        user = post_login(username, password)

        if user is None:
            error = "Incorrect username or password"

        if error is None:
            decoded_user = jwt.decode(user.json()["access_token"], config["SECRET_KEY"], algorithms=config["ALGORITHM"])
            session.clear()
            session["user_id"] = decoded_user["sub"]
            session["access_token"] = user.json()["access_token"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            post_signup(username, password, email)
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view
