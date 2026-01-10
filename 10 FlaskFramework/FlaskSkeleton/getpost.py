# WSGI application
from flask import Flask, render_template, request

# create an instance of the Flask class
app = Flask(__name__)

# route: home page
@app.route("/")
def home():
    return "Hello, Flask is working!"

# route: index page
@app.route("/index", methods=["GET"])
def index():
    return "hello"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Example: read form inputs
        name = request.form.get("name")
        return f"Hello {name}, how are you "
    return render_template("form.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        # Example: read form inputs
        name = request.form.get("name")
        return f"Hello {name}, how are you "
    return render_template("form.html")

# app starts from here
if __name__ == "__main__":
    app.run(debug=True)
