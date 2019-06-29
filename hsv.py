import cv2
import imutils
from imutils.video import VideoStream


greenLower = (86, 6, 6)
greenUpper = (188, 255, 54)
vs = VideoStream(src=0).start()
while True:
    frame = vs.read()
    if frame is None:
        break
    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #mask = cv2.inRange(hsv, (168, 217, 5), (168, 217, 14))
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow("Frame1", mask)
    cv2.imshow("Frame2", hsv)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.waitKey()
cv2.destroyAllWindows()
