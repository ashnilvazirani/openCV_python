import cv2  as cv
import numpy as np
path ="/Users/ashnilvazirani/Downloads/"
photoName = path + "photo.jpg"
image = cv.imread(photoName) 
# cv.imshow('me', image) 
def translateImage(img, x,y):
    translateMatrix=np.float32([[1,0,x], [0,1,y]])
    dimension = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, translateMatrix, dimension)

def rotateImage(image, angle, rotPoint =None):
    (height, width) = image.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(image, rotMat, dimension)

# translateed = translateImage(image, 100,100)
# cv.imshow('I am translated', translateed)

rotated = rotateImage(image, 45)
cv.imshow('I am rotated', rotated)
cv.waitKey(0)