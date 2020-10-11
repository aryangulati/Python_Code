import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
img=cv2.imread("test.jpg")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.5,3)


for face in faces:
    x,y,w,h=face
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    
cv2.imshow("img_window",img)   
cv2.waitKey() 