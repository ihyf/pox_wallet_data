# coding: utf-8
from create_app import app
from flask import render_template


@app.route('/privacy_agreement')
def privacy_agreement():
    return render_template("index.html")


@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
