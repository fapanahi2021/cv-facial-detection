#Import Library
import cv2

#Capture Video
our_video = cv2.VideoCapture(0)

#Check if loaded correctly
check, frame = our_video.read()
print(check, "\n", frame)

#release video
our_video.release()