from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hello CodeWala :)</h1>"

@app.route("/home", methods=["GET"])
def frontend():
    return render_template("index.html")