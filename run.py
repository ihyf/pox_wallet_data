# coding: utf-8
import os
from create_app import app
from flask import render_template
from flask import request, jsonify, send_from_directory, abort


@app.route('/privacy_agreement')
def privacy_agreement():
    return render_template("index.html")


@app.route('/send_tera')
def send_tera():
    return render_template("send_tera.html")


@app.route('/')
def hello():
    return "hello"


@app.route('/download_file/<filename>')
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('static/files', filename)):
            return send_from_directory('static/files', filename, as_attachment=True)
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
