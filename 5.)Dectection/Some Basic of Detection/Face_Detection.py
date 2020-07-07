import cv2

cam=cv2.VideoCapture(0)

#intialising Cascade Classifier with fileName
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") 
#see where your file is ??

while True:
    ret, frame = cam.read() #Status-->True/False #Frame
    
    if not ret:
        continue
    #(Detecting) Find all the faces in the frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # bgr -> grayscale conversion
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    #faces = face_cascade.detectMultiScale(frame, 1.3, 5) # Frame, Scaling Factor, Neighbors
    
    
    
    for face in faces:
        x,y,w,h=face #Tuple unpack
        
        #Drawing rectangle boundary
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #  Frame, Start, End, Color,Thickness
        
        face_only=frame[y:y+h,x:x+w]
        cv2.imshow("Face Selection", face_only)
        
    cv2.imshow("Feed", frame)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

    
 
