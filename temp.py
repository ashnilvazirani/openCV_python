
# Python program to explain cv2.imshow() method  
  
# importing cv2  
import cv2  as cv
path ="/Users/ashnilvazirani/Downloads/"
photoName = path + "photo.jpg"
image = cv.imread(photoName) 
cv.imshow('me', image) 

#waits for user to press any key  
#(this is necessary to avoid Python kernel form crashing) 
videoName=path+"viideoRead.MOV"  
capture = cv.VideoCapture(videoName)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()  