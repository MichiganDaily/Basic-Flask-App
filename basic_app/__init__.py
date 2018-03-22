from flask import Flask, render_template
import flask_sqlalchemy
import os

SQLAlchemy = flask_sqlalchemy.SQLAlchemy

basic_app = Flask(__name__)
if os.name == 'nt':
    # Windows doesn't follow the unix tmp folder path, Use APPDATA Temp folder instead
    appdata = os.getenv('APPDATA').split("\\")
    path = "sqlite:///" + "\\".join(appdata[0:4])
    basic_app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(path, "Local\\Temp\\demo.db")
else:
    # Use the standard tmp folder for all Linux/ MAC OS machines
    basic_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/demo.db'

basic_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
basic_app.config['DEBUG'] = False
db = SQLAlchemy(basic_app)

import basic_app.schema as schema

db.create_all()

test_user = schema.Users("Michael Hess")
db.session.add(test_user)
db.session.commit()


@app.route("/")
def index():
    first_user = schema.Users.query.first()
    return "Hello %s" % first_user.name
