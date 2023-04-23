from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

from  hubconf import custom
model = custom(path_or_model='droned13k.pt')
#model = custom(path_or_model='yolov7.pt')
model.conf = 0.5

#cap = cv2.VideoCapture(1)
#cap.set(cv2.CAP_PROP_EXPOSURE, 1000)

@app.route('/')
def main_page():
     return render_template('index.html')

@app.route('/time_line')
def main_page():
     return render_template('timeline.html')

@app.route('/astro_cam')
def astro_cam():
     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():
     cap = cv2.VideoCapture(1)
     cap.set(cv2.CAP_PROP_EXPOSURE, 500)
     while True:
        success, frame = cap.read()  # read the camera frame

        results = model(frame)
        f2 = np.squeeze(results.render())     

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', f2)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
     
