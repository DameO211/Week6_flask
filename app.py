from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/treats/')
def admin():
    return render_template("dog_bone.html")


@app.route('/bath/')
def bath():
    return render_template("bath.html")


@app.route('/paws/')
def paws():
    return render_template("Doggie_feet.html")


if __name__ == '__main__':
    app.run(debug=True, port='3000', host='0.0.0.0')