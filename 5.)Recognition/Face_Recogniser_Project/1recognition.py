import cv2
import numpy as np

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


skip = 0

while True:
    ret,frame = cam.read()
    if ret==False:
        continue
        
    cv2.imshow("Frame",frame)
    
    
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    print(faces)
    
    
    
    #store every 10th faces
    if skip%10==0:
        #store the 10 face later on 
        pass
    
    
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
