import cv2
from collections import deque
from imutils.video import VideoStream
import numpy as np
import imutils
import time

face_cascade = cv2.CascadeClassifier('/home/navaneeth/work/gui_forcv/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/navaneeth/work/gui_forcv/haarcascade_eye.xml')
class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        #frame = imutils.resize(image, width=600)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        #center = None
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
