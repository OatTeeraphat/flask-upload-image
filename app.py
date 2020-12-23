import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def upload_page():
    return render_template("index.html");


@app.route("/edit", methods=["GET"])
def edit_page():
    
    preview = [
        "http://lorempixel.com/1920/1080/transport/1",
        "http://lorempixel.com/1920/1080/transport/2",
        "http://lorempixel.com/1920/1080/transport/3"
    ]

    preview_config = [
        {"caption": "transport-1.jpg", "url": "http://0.0.0.0:5000/delete?id=1", "key": 1},
        {"caption": "transport-2.jpg", "url": "http://0.0.0.0:5000/delete?id=2", "key": 2},
        {"caption": "transport-3.jpg", "url": "http://0.0.0.0:5000/delete?id=3", "key": 3}
    ]

    return render_template("index.html", preview=preview, preview_config=preview_config);


@app.route("/delete", methods=["POST"])
def delete():
    delete = request.args.get('id')
    print('Delete File :', delete)

    return jsonify(success=True)


@app.route("/upload", methods=["POST"])
def insert():
    file = request.files.getlist("file[]")
    print('File :', file)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)