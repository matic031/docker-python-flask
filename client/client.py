import requests
from flask import Flask, send_file, render_template_string
from threading import Thread
import time
import os

app = Flask(__name__)
IMAGE_PATH = "sample.jpeg"


def fetch_image():
    while True:
        try:
            r = requests.get("http://streznik:5000/image")
            with open(IMAGE_PATH, "wb") as f:
                f.write(r.content)
        except Exception as e:
            print("Error fetching image:", e)
        time.sleep(10)


@app.route("/")
def index():
    return render_template_string(
        """
        <html>
        <head><meta http-equiv="refresh" content="10"></head>
        <body>
            <h1>Client Image Viewer</h1>
            <img src="/image.jpeg" width="640"/>
        </body>
        </html>
        """
    )


@app.route("/image.jpeg")
def serve_image():
    return send_file(IMAGE_PATH, mimetype="image/jpeg")


if __name__ == "__main__":
    Thread(target=fetch_image, daemon=True).start()
    app.run(host="0.0.0.0", port=5001)
