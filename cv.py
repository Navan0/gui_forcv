#!/usr/bin/env python
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
# from camera import VideoCamera

face_cascade = cv2.CascadeClassifier('/home/navaneeth/work/gui_forcv/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/navaneeth/work/gui_forcv/haarcascade_eye.xml')

font = cv2.FONT_HERSHEY_SIMPLEX
buffer = 5

greenLower = (9, 130, 132)
greenUpper = (51, 255, 255)
pts = deque(maxlen=buffer)

vs = VideoStream(src=0).start()
# vs =
# frame = VideoCamera()
# frame0, frame = frame.get_frame()
# frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
# frame = imutils.resize(frame, width=600)
time.sleep(2.0)

while True:

    # cv2.imwrite("Frame.png", frame)

    # frame = frame.write(frame.tofile())
    #frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    frame = vs.read()
    cv2.imwrite("Frame.png", frame)
    if frame is None:
        break
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    pts.appendleft(center)

    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(buffer / float(i + 1)) * 2.5)
        if pts[i] < (300, 220):
            cv2.putText(frame, str('Right'), (550, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        elif pts[i] > (300, 220):
            cv2.putText(frame, str('Left'), (3, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 2)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):
        break


def sent_frame():
    # return frame

    cv2.destroyAllWindows()
