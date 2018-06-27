from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def index():
    users = [
                {
                    'name': "jhajhajhajha", 
                    "username": "jhajhajha11"
                },
                {
                    'name': "John",
                    'username': "Johnny"
                },
            ]
    return render_template('index.html', users = users)


if __name__ == "__main__":
    app.run()
