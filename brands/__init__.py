import os
from dotenv import dotenv_values
from flask import Flask
from . import auth, brands


def create_app(test_config=None):
    config = dotenv_values(".env")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=config["SECRET_KEY"],
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    app.register_blueprint(auth.bp)
    app.register_blueprint(brands.bp)

    return app
