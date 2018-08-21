from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:roottoor@localhost/sample'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    # users = [
    #             {
    #                 'name': "jhajhajhajha",
    #                 "username": "jhajhajha11"
    #             },
    #             {
    #                 'name': "John",
    #                 'username': "Johnny"
    #             },
    #         ]
    # return render_template('index.html', users = users)
    return render_template('add_user.html')


if __name__ == "__main__":
    app.run()
