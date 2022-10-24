import cv2 as  cv
import numpy as np

img = cv.imread('Photos/KenKaneki.jpg')
cv.imshow('Ken', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,  img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

masked1 = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked Image 1', masked1)

rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2,  img.shape[0]//2), (img.shape[1]//2 + 200,  img.shape[0]//2 + 200), 255, -1)
cv.imshow('Mask', rectangle)

masked2 = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow('Masked Image 2', masked2)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

ws1 = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shape Image', ws1)

cv.waitKey()