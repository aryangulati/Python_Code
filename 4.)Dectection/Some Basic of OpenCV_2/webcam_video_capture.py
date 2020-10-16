#Video is taken Frame by Frame

import cv2

cap =cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #if we want gray frame just we have give 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret==True: #until we capture frame 
        cv2.imshow("Video Frame",frame)
        cv2.imshow("GRAY Video Frame",gray_frame)
        
        
        
        #Wait for input of each frame will display after 1ms that makes a video
        key=(cv2.waitKey(1) & 0xFF) 
        #as it store 8 bits but waitKey has 32 bit 
        #we are converting32 bit into  8 bit number and comapring with ASCII val of alpha
        if key  ==  ord('q'): #ord("a") gives ASCII value of "a"
            break
            
        
        
        
cap.release()
cv2.destroyAllWindows()        
    
