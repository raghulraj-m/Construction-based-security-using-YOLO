from flask import Flask, render_template, Response
from threading import Thread
import cv2
import base64
from ultralytics import YOLO
import math

app = Flask(__name__)

# YOLO model and classes
model = YOLO("best.pt")
classNames = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person',
               'SUV', 'Safety Cone', 'Safety Vest', 'bus', 'dump truck', 'fire hydrant', 'machinery', 'mini-van',
               'sedan', 'semi', 'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']

def generate_frames():
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

    while True:
        success, frame = cap.read()
        if not success:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = base64.b64encode(buffer)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


def detect_objects(frame):
    input_size = model.model_info["height"]
    frame = cv2.resize(frame, (input_size, input_size))

    results = model(frame)

    for r in results.xyxy[0]:
        x1, y1, x2, y2 = map(int, r[:4])
        print(f"Detected at coordinates: ({x1}, {y1}) - ({x2}, {y2})")

        conf = math.ceil((r[4] * 100)) / 100
        cls = int(r[5])
        current_class = classNames[cls]

        box_color = (0, 0, 255) if current_class == 'NO-Mask' else (0, 255, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 3)

    return frame


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False}).start()
