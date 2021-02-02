import cv2  as cv
path ="/Users/ashnilvazirani/Downloads/"
photoName = path + "photo.jpg"
image = cv.imread(photoName) 
cv.imshow('me', image) 

# image grayScaling
gray  = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow('meGray😂', gray)

blur = cv.GaussianBlur(image, (7,3), cv.BORDER_DEFAULT)
# cv.imshow('meBlur😂', blur)

# cascading edges
canny = cv.Canny(image, 25, 175)
# cv.imshow('Edges', canny)

resized = cv.resize(image, (300, 300), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

cropped = image[0:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)