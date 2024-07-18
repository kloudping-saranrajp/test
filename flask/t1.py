from flask import Flask as f
app = f(__name__)
@app.route("/")
def hello():
    return "<p>Hello</p>"