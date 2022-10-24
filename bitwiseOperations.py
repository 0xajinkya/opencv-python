from curses.textpad import rectangle
from turtle import circle
import numpy as np
import cv2 as cv

blank = np.zeros((400,400), dtype='uint8')

# Draw A Rectangle
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Draw A Circle
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

# Showing Them
cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# Bitwise AND Operator
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('B AND', bitwise_and)

# Bitwise OR Operator
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('B OR', bitwise_or)

# Bitwise XOR Operator
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('B XOR', bitwise_xor)

# Bitwise NOT Operator For Rectangle
bitwise_not_r = cv.bitwise_not(rectangle)
cv.imshow('B NOT For Rectangle', bitwise_not_r)

# Bitwise NOT Operator For Circle
bitwise_not_c = cv.bitwise_not(circle)
cv.imshow('B NOT For Circle', bitwise_not_c)

cv.waitKey()