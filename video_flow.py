import numpy as np
import cv2
import sys
import YOLO_small_tf
from Person import Passenger

yolo = YOLO_small_tf.YOLO_TF()
fps = 24.0
cap = cv2.VideoCapture(sys.argv[1])
vw = int(cap.get(3))
vh = int(cap.get(4))
# for i in range(10): #
#     print(i, cap.get(i))
outv = cv2.VideoWriter(sys.argv[1] + '.processed.mp4', cv2.VideoWriter_fourcc(*'mjpg'), fps, (vw, vh))

inLine = int(6*vh/8)
centerLine = int(5*vh/8)
outLine = int(4*vh/8)

font = cv2.FONT_HERSHEY_SIMPLEX

inCount = 0
outCount = 0
passengers = []
pid = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    results = yolo.analyze_frame(frame)

    for i in passengers:
        i.bday()

    for res in results:
        if res[0] == 'person':
            x = int(res[1])
            y = int(res[2])
            w = int(res[3])//2
            h = int(res[4])//2
            cv2.circle(frame,(x,y), 5, (0,0,255), -1)
            cv2.rectangle(frame,(x-w,y-h),(x+w,y+h),(0,255,0),2)
            print(res)

            if y in range(outLine,inLine):
                new = True
                for i in passengers:
                    if i.near(x, y):
                        i.updateCoords(x, y)
                        new = False
                        if i.wasGoingOut(outLine,inLine) == True:
                            outCount += 1;
                        elif i.going_DOWN(outLine,inLine) == True:
                            inCount += 1;
                        break

                    if i.getState() == '1':
                        i.setDone()

                    if i.timedOut():
                        index = persons.index(i)
                        persons.pop(index)
                        del i

                if new == True:
                    passengers.append(Passenger(pid, x, y, 10))


    cv2.line(frame, (0,inLine), (vw,inLine), (255,0,0), 2)
    cv2.line(frame, (0,centerLine), (vw,centerLine), (0,0,255), 2)
    cv2.line(frame, (0,outLine), (vw,outLine), (0,255,0), 2)

    cv2.putText(frame, "Enter: %d"%inCount, (25, int(vh/10)), font, 0.5, (12, 220, 120))
    cv2.putText(frame, "Exit: %d"%outCount, (25, int(1.2*vh/10)), font, 0.5, (12, 220, 120))

    outv.write(frame)

    cv2.imshow('Frame',frame)
    k = cv2.waitKey(int(1000.0 / fps)) & 0xff
    if k == 27:
        break

cap.release() #release video file
outv.release()
cv2.destroyAllWindows() #close all openCV windows
