from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world"


@app.errorhandler(404)
def page_not_found(e):
    return "ERROR: {} ".format(e),404

if __name__ == '__main__':
    app.run()