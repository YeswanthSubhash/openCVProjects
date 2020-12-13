import cv2
import numpy as np
print("Pakage Imported")
#read image from the folder
img=cv2.imread("Resources/sony.jpg")

width,height=250,350

pts = np.float32([[1,40],[248,96],[1,158],[247,189]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts,pts2)
imageoutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("ImageOutput",imageoutput)
cv2.waitKey(0)