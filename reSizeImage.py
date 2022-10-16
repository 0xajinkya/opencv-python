import cv2 as cv

img = cv.imread('Photos/SoloLeveling.jpg')


#Function To Rescale An Image
def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img_resized = rescaleFrame(img)
cv.imshow('Jin Woo', img)
cv.imshow('Jin Woo Resized', img_resized)

cv.waitKey()