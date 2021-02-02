import cv2  as cv
def chageResolution(width, height):
    # this is used for live video rescale, eg: camera
    capture.set(3, width)
    capture.set(4, height)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
path ="/Users/ashnilvazirani/Downloads/"
videoName=path+"viideoRead.MOV"  
capture = cv.VideoCapture(videoName)
while True:
    isTrue, frame = capture.read()
    reframe = rescaleFrame(frame, 1.5)
    cv.imshow('Video',reframe)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()  