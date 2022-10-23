import cv2 as cv
import numpy as np

img = cv.imread('Photos/KenKaneki.jpg')
cv.imshow('Ken', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r= cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g,blank])
red = cv.merge([blank,blank, r])

# cv.imshow('Blue Ken', b)
# cv.imshow('Green Ken', g)
# cv.imshow('Red Ken', r)

cv.imshow('Blue Ken', blue)
cv.imshow('Green Ken', green)
cv.imshow('Red Ken', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey()