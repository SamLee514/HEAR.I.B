import cv2
from gaze_tracking import GazeTracking
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)





while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "right"
    elif gaze.is_left():
        text = "left"
    elif gaze.is_center():
        text = "center"

    write_to = open("eye_direction.txt","w")
    write_to.write(text)

    cv2.putText(new_frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Demo", new_frame)

    if cv2.waitKey(1) == 27:
        break