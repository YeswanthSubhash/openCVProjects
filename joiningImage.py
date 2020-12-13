import cv2
import numpy as np

img=cv2.imread("Resources/group Photo.JPG")

#horrizontal
imghor=np.hstack([img,img])

#vertical
imagever=np.vstack([img,img])

cv2.imshow("image horizontal",imghor)
cv2.imshow("image vertical",imagever)
cv2.waitKey(0)