import cv2 as cv
import numpy as np

# 1. Painting The Image A Certain Color

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300,:] = 0,0,255
cv.imshow('Red', blank)

blank[:, 300:400] = 0,0,255
cv.imshow('Red', blank)

blank[200:300, 300:400] = 0,0,255
cv.imshow('Red', blank)



#2. Drawing A Rectangle

blank1 = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank1', blank1)

# cv.FILLED == -1
# cv.rectangle(blank1, (0,0), (250, 250), (0,255,0), thickness=cv.FILLED)
cv.rectangle(blank1, (0,0), (blank1.shape[1]//2, blank1.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank1)




#3. Drawing A Circle

blank2 = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank2', blank2)

# cv.circle(blank2, (250, 250), 40, (90,0,255), thickness=3)
cv.circle(blank2, (blank2.shape[1]//2, blank2.shape[0]//2), 40, (90,0,255), thickness=-1)
cv.imshow('Cirlce', blank2)




#4. Drawing A Line

blank3 = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank2', blank3)

# cv.line(blank3, (0,0), (blank3.shape[1]//2, blank3.shape[0]//2), (255,255,255), thickness=5)
cv.line(blank3, (100,100), (blank3.shape[1]//2+50, blank3.shape[0]//2+150), (255,255,255), thickness=5)
cv.imshow('Line', blank3)




#5. Writing Text On An Image

blank4 = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank2', blank4)

cv.putText(blank4, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank4)



cv.waitKey(0)

