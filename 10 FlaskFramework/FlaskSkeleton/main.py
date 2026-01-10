# WSGI application
from flask import Flask,render_template

# create an instance of the Flask class
app = Flask(__name__)

# route: home page
@app.route("/")
def home():
    return "<html><H1> Hello, Flask is working! </H1></html>"

# route: index page
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
# app starts from here
if __name__ == "__main__":
    app.run(debug=True)

