from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sreality.db"
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return render_template("index.html", content="Hello World!")


if __name__ == "__main__":
    app.run(port=5115, debug=True)
    db.create_all()
