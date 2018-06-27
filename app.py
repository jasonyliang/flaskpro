from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello! World.</h1>"


@app.route('/homepage')
def homepage():
    return "This is a homepage xDD"



if __name__ == "__main__":
    app.run()
