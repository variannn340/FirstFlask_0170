from flask import Flask
from markupsafe import escape
app=Flask(__name__)
@app.route('/')
def hello():
    return "<p>Hello, World!"

def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"



