import cv2
print("Pakage Imported")

#read from webcam
cap=cv2.VideoCapture(0)

#set width to the web cam capture
cap.set(3,640)
#set height to the web cam capture
cap.set(4,480)
#set brightness
cap.set(10,90)

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break