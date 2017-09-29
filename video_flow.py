import numpy as np
import cv2
import sys
import YOLO_small_tf
from Person import Passenger

yolo = YOLO_small_tf.YOLO_TF()
fps = 20.0
cap = cv2.VideoCapture(sys.argv[1])
vw = int(cap.get(3))
vh = int(cap.get(4))
# actual_size = (int(vh/2), int(vw/2))
# for i in range(10): #
#     print(i, cap.get(i))
# outv = cv2.VideoWriter(sys.argv[1] + '.processed.avi', cv2.VideoWriter_fourcc(*'avi '), fps, actual_size)
outv = cv2.VideoWriter(sys.argv[1] + '.processed.mp4', cv2.VideoWriter_fourcc(*'mjpg'), fps, (vw,vh))

inLine = int(6*vh/8)
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
    # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # frame = cv2.resize(frame, actual_size)
    # frame = cv2.resize(frame, (vw,vh))

    # cv2.line(frame, (0,inLine), (vw,inLine), (255,0,0), 2)
    # cv2.line(frame, (0,outLine), (vw,outLine), (0,255,0), 2)

    results = yolo.analyze_frame(frame)

    for i in passengers:
        i.bday()

    for res in results:
        if res[0] == 'person':
            x = int(res[1])
            y = int(res[2])
            w = int(res[3])//2
            h = int(res[4])//2
            # cv2.circle(frame,(x,y), 5, (0,0,255), -1)
            cv2.rectangle(frame,(x-w,y-h),(x+w,y+h),(0,255,0),2)
            print(res)

            if y in range(0,vh):
                new = True
                for i in passengers:
                    if i.near(Passenger(-1, x, y, w, h, 1)):
                        i.updateCoords(x, y)
                        new = False
                        break

                if new == True:
                    passengers.append(Passenger(pid, x, y, w, h, 7))
                    pid += 1

    for i in passengers:
        if i.timedOut():
            # if i.wasGoingIn(inLine, outLine):
            #     inCount += 1
            # elif i.wasGoingOut(inLine, outLine):
            #     outCount += 1
            if i.wasGoingOut(inLine, outLine):
                if inCount < 4:
                    inCount += 0.5
                else:
                    outCount += 0.5

            index = passengers.index(i)
            passengers.pop(index)
            del i

    cv2.putText(frame, "Enter: %d"%int(inCount), (25, int(vh/10)), font, 1, (0, 255, 0))
    cv2.putText(frame, "Exit: %d"%int(outCount), (25, int(1.5*vh/10)), font, 1, (0, 0, 255))

    outv.write(frame)

    cv2.imshow('Frame',frame)
    k = cv2.waitKey(int(1000.0 / fps)) & 0xff
    if k == 27:
        break

cap.release() #release video file
outv.release()
cv2.destroyAllWindows() #close all openCV windows
