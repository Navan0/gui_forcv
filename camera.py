import cv2
from imutils.video import VideoStream
# from collections import deque
# import numpy as np
# import imutils
# import time


class VideoCamera(object):
    def __init__(self):
        self.video = VideoStream(src=0).start()

    def get_frame(self):
        face_cascade = cv2.CascadeClassifier('/home/navaneeth/work/gui_forcv/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('/home/navaneeth/work/gui_forcv/haarcascade_eye.xml')
        frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        ret, jpeg = cv2.imencode('.png', frame)
        return (jpeg.tobytes(), jpeg)
