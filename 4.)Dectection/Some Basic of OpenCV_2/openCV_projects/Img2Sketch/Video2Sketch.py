#Video is taken Frame by Frame

import cv2

cap =cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #if we want gray frame just we have give 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Invert the frame
    inverted_frame=255-gray_frame
    #Blur the frame by Gaussian function
    blurred_frame=cv2.GaussianBlur(inverted_frame,(21,21),0)#kernel size (21,21)
    #sigma value is 0
    #invert the blurred frame
    inverted_blurred=255-blurred_frame

    sketchy_img=cv2.divide(gray_frame,inverted_blurred,scale=256.0)

    
    if ret==True: #until we capture frame 
        cv2.imshow("Video Frame",frame)
        cv2.imshow("GRAY Video Frame",sketchy_img)
        
        
        
        #Wait for input of each frame will display after 1ms that makes a video
        key=(cv2.waitKey(1) & 0xFF) 
        #as it store 8 bits but waitKey has 32 bit 
        #we are converting32 bit into  8 bit number and comapring with ASCII val of alpha
        if key  ==  ord('q'): #ord("a") gives ASCII value of "a"
            break
            
        
        
        
cap.release()
cv2.destroyAllWindows()        
    
