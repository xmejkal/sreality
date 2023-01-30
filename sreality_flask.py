from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", content="Hello World!")


if __name__ == "__main__":
    app.run(port=5115)
