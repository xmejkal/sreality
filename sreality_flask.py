from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

import settings

# App and DB
app = Flask(__name__)
app.config.from_pyfile("settings.py")
db = SQLAlchemy(app)


# Models
class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    photos = db.relationship("Photo", backref="flat", lazy=True)

    def __repr__(self) -> str:
        return f"Flat('{self.title}')"


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable=False)
    flat_id = db.Column(db.Integer, db.ForeignKey("flat.id"), nullable=False)
    flat = db.relationship("Flat", backref=db.backref("photos", lazy=True))

    def __repr__(self) -> str:
        return f"Photo('{self.url}')"


# Routes
@app.route("/")
def hello():
    return render_template("index.html", content="Hello World!")


# Run
if __name__ == "__main__":
    app.run(port=5115, debug=True)
    db.create_all()
