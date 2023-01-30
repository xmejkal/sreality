from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sreality.db"
db = SQLAlchemy(app)


class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    photos = db.relationship("Photo", backref="flat", lazy=True)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable=False)
    flat_id = db.Column(db.Integer, db.ForeignKey("flat.id"), nullable=False)
    flat = db.relationship("Flat", backref=db.backref("photos", lazy=True))


@app.route("/")
def hello():
    return render_template("index.html", content="Hello World!")


if __name__ == "__main__":
    app.run(port=5115, debug=True)
    db.create_all()
