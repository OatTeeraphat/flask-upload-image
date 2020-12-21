import os
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.getlist("file[]")
    print('File :', file)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)