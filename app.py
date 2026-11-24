from flask import Flask
from markupsafe import escape
app=Flask(__name__)
@app.route('/')
def hello():
    return "<p>Hello, World!"

def about():
    return "About us"

