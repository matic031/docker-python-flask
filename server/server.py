from flask import Flask, send_file
import time
import cv2

app = Flask(__name__)

@app.route('/image')
def get_image():
    image = cv2.imread("sample.jpg")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(image, timestamp, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imwrite("timestamped.jpg", image)
    return send_file("timestamped.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
