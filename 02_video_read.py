import cv2
import numpy as np

cap = cv2.VideoCapture('00006.MTS')

while True:
    ret,frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame,(4*192,4*108))
    cv2.rectangle(frame,(0,0),(50,100),(0,255,0),-1)
    cv2.line(frame,(0,0),(50,100),(0,0,255),10 )
    cv2.circle(frame, (50,50),50,(255,0,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"OpenCV Rocks!",(200,200),font,2,(255,255,255),cv2.LINE_AA)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()