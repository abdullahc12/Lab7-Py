import cv2
import numpy as np

photo= cv2.imread("resim1.jpg")

cv2.imshow('Image', photo)

cv2.waitKey(0)

b, g, r = cv2.split(photo)

cv2.imshow('Blue Channel', b)

cv2.imshow('Green Channel', g)

cv2.imshow('Red Channel', r)
cv2.waitKey(0)

g.fill(0)

result = cv2.merge((b, g, r))

cv2.imshow('Red and Blue Image', result)
cv2.waitKey(0)

cv2.destroyAllWindows()
