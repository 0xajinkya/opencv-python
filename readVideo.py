import cv2 as cv

#Getting Video In A Variable
capture = cv.VideoCapture('Videos/BorutoUzumaki.mp4')

#Reading The Video Frame By Frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    #Breaking Out Of The Loop If 'd' Is Pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()