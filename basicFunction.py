import cv2 as cv 

img = cv.imread('Photos/KenKaneki.jpg')
cv.imshow('Ken', img)

#Converting To Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow('Gray Ken', gray)

# Gaussian Blur To Image
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred Ken', blur)

#Edge Cascading
canny = cv.Canny(img, 125,175)
cv.imshow('Canny Edge Ken', canny)

#Removing Unnecessary Edges
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edge Ken', canny)

#Dilating Image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated Image', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow('Eorded', eroded)

#Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#Cropping
# cropped = img[:, :]
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey()