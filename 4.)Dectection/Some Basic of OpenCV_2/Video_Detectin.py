import cv2
#Each video is of series of Frame
cam = cv2.VideoCapture(0)#cv2.VideoCapture("./video.mp4")#cam =cv2.VideoCapture("path")
#https://github.com/opencv/opencv/tree/master/data/haarcascades

model = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")

while True:
	ret, frame = cam.read()
	if ret == True:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # bgr -> grayscale conversion
		faces = model.detectMultiScale(gray_frame, 1.3, 0)
        #detectMultiScale(gray_frame, 1.3, 0) it has 2 parameter 
        #scaling factor and no. of neighbors
		for face in faces:
			x, y, w, h = face

			cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
		cv2.imshow("window", frame)
		key = cv2.waitKey(1) #1ms wait by waitkey function
		if key == ord("q"):
			break
	else:
		break

cam.release()
cv2.destroyAllWindows()