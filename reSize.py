import cv2 as cv

# img = cv.imread('Photos/SoloLeveling.jpg')
# cv.imshow('Jin Woo', img)

#Function To Rescale An Image
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#Reading Video
capture = cv.VideoCapture('Videos/BorutoUzumaki.mp4')

#Reading The Video Frame By Frame
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    # print(frame)

    cv.imshow('Video', frame)

    cv.imshow('Video', frame_resized)

    #Breaking Out Of The Loop If 'd' Is Pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()