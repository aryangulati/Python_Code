#simple opencv
import cv2

image=cv2.imread("bob.jpg")

cv2.imshow("Bob The Builder",image)
cv2.waitKey(1000) #it hold process execution for new window of img
# and it contain millisecond parameter put 1000