# Recognise Faces using some classification algorithm - like  KNN


# 1. load the training data (numpy arrays of all the persons)
		# x- values are stored in the numpy arrays
		# y-values we need to assign for each person
# 2. Read a video stream using opencv
# 3. extract faces out of it
# 4. use knn to find the prediction of face (int)
# 5. map the predicted id to name of the user 
# 6. Display the predictions on the screen - bounding box and name

#its easy way to do face recognition and not effective 
#we can to do by Cnn (deep learning)




import os
import numpy as np
import cv2



dataset_path = "./data1/"

face_data = []
labels = []

for fx in os.listdir(dataset_path):
    if fx.endswith(".npy"):
        l = fx.split(".")[0]
        
        face_item = np.load(dataset_path + fx)#Load arrays or pickled objects from ``.npy``, ``.npz`` or pickled files.
        #Dataset path + file name of npy we are giving above
        # print(face_item.shape)
        print("loaded " , l) #so it can tell which all have loaded
        
        face_data.append(face_item)
        # appending labels #times => faces
        for i in range(face_item.shape[0]): #we are appending labels no of time faces are appended
            labels.append(l)


X = np.concatenate(face_data, axis =0)  #we are concatenate data so we can input in kNN 
#here we are adding both the images in np array
Y = np.array(labels)

print(X.shape)
print(Y.shape)

# KNN CODE 
def distance(pA, pB):
    return np.sum((pB - pA)**2)**0.5


def kNN(X, y, x_query, k = 5):


	"""
	X - > (m, 30000)  np array
	y - > (m,) np array
	x_query -> (1,30000) np array
	k -> scaler  int
	do knn for classification
	"""
	m = X.shape[0]
	distances = []

	for i in range(m):
		dis = distance(x_query, X[i])
		distances.append((dis, Y[i]))
	    
	distances = sorted(distances)
	distances = distances[:k]

	distances = np.array(distances)
	labels = distances[:, 1]


	uniq_label, counts = np.unique(labels, return_counts=True)

	pred = uniq_label[counts.argmax()]


	return pred

# TEST FACE RECOG


cam = cv2.VideoCapture(0) #this is for video capturing

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")




while True:
    ret, frame = cam.read()
    if ret == False:
        continue
        
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # bgr -> grayscale conversion
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    
    

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
        offset = 10
        face_section = frame[y-offset : y+h+offset , x-offset : x+w+offset]
        face_section = cv2.resize(face_section , (100 , 100))
        
        name = kNN(X, Y, face_section.reshape(1,-1)) #in x_query we have to pass face_section but we have to resize
        #it into 1,100,100,3 so we can reshape or .flatten() int0 -1 or 30000
        
        cv2.putText(frame, name.title(), (x, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2, cv2.LINE_AA)
        #check .puText()? check docs
        #putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    
    cv2.imshow("window", frame)

    key = cv2.waitKey(1) # 1ms
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

