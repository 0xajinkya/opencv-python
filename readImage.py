import cv2 as cv

#Reading Image
img = cv.imread('Photos/KenKaneki.jpg')

#Showing Image
cv.imshow('Ken Kaneki',img)

#Keeping Image
cv.waitKey()