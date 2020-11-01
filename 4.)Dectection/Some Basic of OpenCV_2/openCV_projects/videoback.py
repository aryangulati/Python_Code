import cv2
import numpy as np
import sys

def resize(dst,img):
	width = img.shape[1]
	height = img.shape[0]
	dim = (width, height)
	resized = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)
	return resized

video = cv2.VideoCapture(0)
oceanVideo = cv2.VideoCapture("video.mp4")
ret , frame = video.read()
#here we are just storing background img in frame and using its first frame
flag = 0

while(1):
        ret , img = video.read()
        ret2, bg = oceanVideo.read()
        bg = resize(bg,frame)
        if flag==0:
                frame = img
        # create a mask
        diff1=cv2.subtract(img,frame)
        diff2=cv2.subtract(frame,img)
        diff = diff1+diff2
        diff[abs(diff)<100.0]=0
        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) < 10] = 0
        fgmask = gray.astype(np.uint8)
        fgmask[fgmask>0]=255
        #invert the mask
        fgmask_inv = cv2.bitwise_not(fgmask)
        #use the masks to extract the relevant parts from FG and BG
        fgimg = cv2.bitwise_and(img,img,mask = fgmask)
        bgimg = cv2.bitwise_and(bg,bg,mask = fgmask_inv)
        #combine both the BG and the FG images
        dst = cv2.add(bgimg,fgimg)
        cv2.imshow('Background Removal',dst)
        key = cv2.waitKey(5) & 0xFF
        if ord('q') == key:
                break
        elif ord('d') == key:
                flag = 1
                print("Background Captured")
        elif ord('r') == key:
                flag = 0
                print("Ready to Capture new Background")

cv2.destroyAllWindows()
video.release()
#return jpeg.tobytes()