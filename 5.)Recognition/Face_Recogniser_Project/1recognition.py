import cv2
import numpy as np

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


skip = 0
face_data = []
#store data in array of img in data folder 
dataset_path = './data/' 

file_name=input("Enter the name of the person :")

while True:
    ret,frame = cam.read()
    
    
    if ret==False:
        continue
        
#     cv2.imshow("Frame",frame)
    
    
    
#     faces = face_cascade.detectMultiScale(frame,1.3,5)
#     print(faces)
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)



    faces = face_cascade.detectMultiScale(frame,1.3,5)
    if len(faces)==0:
        continue

    
    #make a rectangle box around faces (bounding box)
    #pick the last face (because it is the largest face acc. to area (f[2]*f[3]))
    for face in faces[-1:]:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        
        
        #Extract (Crop out the required face ): Region of interest we want !!
        offset =10 #padding of 10 pixel around the face
        #Frame[Y,X]
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset] 
        face_section =cv2.resize(face_section,(100,100))
        
        
        skip+=1
        if skip%10==0:
            face_data.append(face_section)
            print(len(face_data)) #this store and print every 10th face 
#     #store every 10th faces
#     if skip%10==0:
#         #store the 10 face later on 
#         pass
        
    
    
    cv2.imshow("Frame",frame)
    #we have took RGB img so   no. of frame x size(10000) x 3 
    cv2.imshow("face section",face_section)
    
    
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

#Convert our face list array into a numpy array
face_data =np.asanyarray(face_data)
face_data =face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

#save this data into file system
np.save(dataset_path+file_name+".npy",face_data)

print("Data succesfully saved at "+dataset_path+file_name+".npy")
        
        
cam.release()
cv2.destroyAllWindows()
