import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')



cap = cv2.VideoCapture(0)
ret,img = cap.read()
while(ret):
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,5,1,1) #filter for removing impurities
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(len(faces)>0):
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            gray_img = gray[y:y+h,x:x+w]
            clr_img = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(clr_img,1.3,5)
            if(len(eyes)>=1):
                cv2.putText(img, "Not Sleeping", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)
            else:
                cv2.putText(img, "Sleeping", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)                  
    else:
        cv2.putText(img,"Sleeping",(100,100),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255) ,2)
    cv2.imshow('img',img)
    a = cv2.waitKey(1)
    if(a==ord('q')):
        break
    


cap.release()
cv2.destroyAllWindows()