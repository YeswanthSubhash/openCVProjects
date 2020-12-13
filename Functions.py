import cv2
import numpy as np

#readImage
img=cv2.imread("Resources/group Photo.JPG")
kernel=np.ones((5,5),np.uint8)

#convert the image to Gray
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#convert the image to blur
imgBlur=cv2.GaussianBlur(imgGray,(9,9),0)
#convert to canny Image
imgCanny=cv2.Canny(imgGray,150,200)
#convert to Dialation Image
imageDialation=cv2.dilate(imgCanny,kernel,iterations=1)
#convert to erodade Image
imageErodaded=cv2.erode(imageDialation,kernel,iterations=1)

cv2.imshow("GreyIamge",imgGray)
cv2.imshow("BlurIamge",imgBlur)
cv2.imshow("CannyIamge",imgCanny)
cv2.imshow("DialationIamge",imageDialation)
cv2.imshow("ErodadeIamge",imageErodaded)
cv2.waitKey(0)