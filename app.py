from flask import Flask
app = Flask("__name__")
@app.route("/")
def index():
	return "hello zayan papa love u"

@app.route("/<string:name>")
def mm(name):
	name = name.capitalize()
	return f"hello {name}"
