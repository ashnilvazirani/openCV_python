import cv2  as cv
path ="/Users/ashnilvazirani/Downloads/"
photoName = path + "photo.jpg"
image = cv.imread(photoName) 
cv.imshow('me', image) 
