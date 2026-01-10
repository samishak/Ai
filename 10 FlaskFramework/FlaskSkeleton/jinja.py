##building url dynamically 
#variable rule
#jinja 2 template engine 
###jinja 2 template engine 
'''
{{}}expression to print output in html 
{%...%}conditions for loops 
{#...#}this is for comments 
'''

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

##variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template("result.html",result=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
        
    exp={'score':score,"res":res}
    
    return render_template("result1.html",results=exp)

# app starts from here
if __name__ == "__main__":
    app.run(debug=True)
