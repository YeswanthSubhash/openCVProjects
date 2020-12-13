import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
print(img)
#img[:]=255,0,0 #fill with blue
#img[200:300,100:200]=0,255,0

# draw line
#cv2.line(img,(0,0),(200,300),(0,0,255),3)
# draw a diagonal line
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),3)
# rectabgle
cv2.rectangle(img,(10,10),(200,300),(255,0,255),3)

#fill the recatangle
cv2.rectangle(img,(10,10),(200,300),(0,200,250),cv2.FILLED)

# circle
cv2.circle(img,(400,50),30,(255,255,0),5)

#Text
cv2.putText(img,"OPEN CV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)