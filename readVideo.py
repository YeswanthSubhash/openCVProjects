import cv2
print("Pakage Imported")

#read video from resource
cap=cv2.VideoCapture("Resources/test_video.mp4")


while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break