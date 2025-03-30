from flask import Flask, send_file
import os

app = Flask(__name__)


@app.route("/image")
def get_image():
    return send_file("sample.jpeg", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
