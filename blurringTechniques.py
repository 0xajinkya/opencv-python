import cv2 as cv

img = cv.imread('Photos/KenKaneki.jpg')
cv.imshow('Ken', img)

# 1. Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# 2. Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# 3. Median Blur
med = cv.medianBlur(img, 3)
cv.imshow('Median Blur', med)

# 4. Bilateral Blur
bil = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral Blur', bil)
cv.waitKey()