from flask import flask
app = Flask(__name__)

@app.route('/')
def hello_DT():
	return 'Hello, DT! Team1Members.'