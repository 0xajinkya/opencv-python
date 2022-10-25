import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/KenKaneki.jpg')
cv.imshow('Ken', img)

# 1. Computing Grayscale Histogram

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Ken', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Cirlce', circle)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Mask', mask)

# # gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No. Of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# 2. Computing Color Histogram

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Ken', masked)

plt.figure()
plt.title('Colorful Histogram')
plt.xlabel('Bins')
plt.ylabel('No. Of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
#   hist = cv.calcHist([img], [i], mask, [256], [0,256])
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0, 256) 

plt.show()

cv.waitKey()