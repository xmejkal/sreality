import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__)
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://"
    + os.environ.get("POSTGRES_USER")
    + ":"
    + os.environ.get("POSTGRES_PASSWORD")
    + "@"
    + os.environ.get("POSTGRES_HOST")
    + ":"
    + os.environ.get("POSTGRES_PORT")
    + "/"
    + os.environ.get("POSTGRES_DB")
)


db = SQLAlchemy(app)

# Models
class Flat(db.Model):
    __tablename__ = "flats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    photo_url = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Flat('{self.name}')"


# Routes
@app.route("/")
def hello():
    with app.app_context():
        db.create_all()
    flats = Flat.query.all()
    return render_template("index.html", flats=flats)


# Run
if __name__ == "__main__":
    app.run(port=5115, debug=True)
