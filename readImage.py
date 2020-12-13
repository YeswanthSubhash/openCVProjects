import cv2
print("Pakage Imported")
#read image from the folder
img=cv2.imread("Resources/group Photo.JPG")

#display the image
cv2.imshow("output",img)

#delay for display image infinity
cv2.waitKey(0)