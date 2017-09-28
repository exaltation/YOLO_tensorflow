import numpy as np
import cv2
import sys
import YOLO_small_tf

yolo = YOLO_small_tf.YOLO_TF()
fps = 30.0
cap = cv2.VideoCapture(sys.argv[1])
vw = int(cap.get(3))
vh = int(cap.get(4))
# for i in range(10): #
#     print(i, cap.get(i))
outv = cv2.VideoWriter(sys.argv[1] + '.processed.mp4', cv2.VideoWriter_fourcc(*'mjpg'), fps, (vw, vh))

inLine = 7*vh//8
outLine = 5*vh//8

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    results = yolo.analyze_frame(frame)

    for res in results:
        if res[0] == 'person':
            x = int(res[1])
            y = int(res[2])
            w = int(res[3])//2
            h = int(res[4])//2
            cv2.circle(frame,(x,y), 5, (0,0,255), -1)
            cv2.rectangle(frame,(x-w,y-h),(x+w,y+h),(0,255,0),2)
            print(res)

    cv2.line(frame, (0,inLine), (vw,inLine), (255,0,0), 2)
    cv2.line(frame, (0,outLine), (vw,outLine), (0,255,0), 2)

    outv.write(frame)

    cv2.imshow('Frame',frame)
    k = cv2.waitKey(1000.0 / fps) & 0xff
    if k == 27:
        break

cap.release() #release video file
outv.release()
cv2.destroyAllWindows() #close all openCV windows
