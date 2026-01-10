# WSGI application
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# route: home page
@app.route("/")
def home():
    return " Hello, Flask is working!"

# route: index page
@app.route("/index")
def index():
    return "hello"

# app starts from here
if __name__ == "__main__":
    app.run(debug=True)
