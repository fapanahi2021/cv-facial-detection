import cv2
import numpy as np

faceXML = cv2.CascadeClassifier('face.xml')
eyeXML = cv2.CascadeClassifier('eye.xml')

cap= cv2.VideoCapture()

while True:
    _, frame= cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceXML.detectMultiscale(gray)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+y,y+h), (255, 0,0), 2)
        roi_gray = gray[y:y+h, x:x+h]
        roi_color = frame[y:y+h, x:x+w]
        eyes= eyeXML.detectMultiscale(roi_gray)
        for (ex,ey,eh,ew) in eyes:
          cv2.rectangle(roi_color, frame, (ex,ey), (ex+y,ey+h), (255, 0,0), 2)
          
    cv2.imshow('face', frame)
    k = cv2.waitKey(27) & 0xFF
    if (k==27):
        break


cv2.destroyAllWindows() 
cap.release           
            
    

