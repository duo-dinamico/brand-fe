from flask import Flask, render_template, session, request, redirect, url_for
from markupsafe import escape
from .api.user import post_login

app = Flask(__name__)


@app.route("/")
def index():
    if "username" in session:
        return f'Logged in as {session["username"]}'
    return "You are not logged in"


@app.route("/signup", methods=["POST"])
def signup():
    return "Username e password"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("login.html.j2")


@app.route("/brands")
def list_all_brands():
    return "A list of all the brands"


@app.route("/brands/<string:brand_id>")
def list_one_brand(brand_id):
    return f"This is just the brand with the id: {escape(brand_id)}"
