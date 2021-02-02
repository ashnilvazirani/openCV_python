import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow('Temp', blank)
# blank[200:300, 400:500]=0,0,255
# cv.imshow('Red', blank)
cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (255,0,0), thickness=-1)
# cv.imshow('Rectangle', blank)
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), (40), (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)
cv.line(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (0,255,0), thickness=3)
cv.putText(blank, "hello", (255,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255, 255), 2)
cv.imshow('Shapes', blank)
cv.waitKey(0)