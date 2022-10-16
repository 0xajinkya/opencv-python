import cv2 as cv

#Function To Change Resolution Of Video/ Images/ Live Videos
def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Another Function To Change Resolution Of Live Videos Only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


#Reading Video
capture = cv.VideoCapture('Videos/BorutoUzumaki.mp4')

# Reading The Video Frame By Frame
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    #Original Video
    cv.imshow('Video', frame)
    
    #Resized Video
    cv.imshow('Video Resized', frame_resized)

    #Breaking Out Of The Loop If 'd' Is Pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
