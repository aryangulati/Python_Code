# Recognise Faces using some classification algorithm - like  KNN


# 1. load the training data (numpy arrays of all the persons)
		# x- values are stored in the numpy arrays
		# y-values we need to assign for each person
# 2. Read a video stream using opencv
# 3. extract faces out of it
# 4. use knn to find the prediction of face (int)
# 5. map the predicted id to name of the user 
# 6. Display the predictions on the screen - bounding box and name



import os
import numpy as np
import cv2



dataset_path = "./data/"

face_data = []
labels = []

for fx in os.listdir(dataset_path):
    if fx.endswith(".npy"):
        l = fx.split(".")[0]
        
        face_item = np.load(dataset_path + fx)
        # print(face_item.shape)
        print("loaded " , l)
        
        face_data.append(face_item)
        # appending labels #times => faces
        for i in range(face_item.shape[0]):
            labels.append(l)


X = np.concatenate(face_data, axis =0)
Y = np.array(labels)

print(X.shape)
print(Y.shape)

