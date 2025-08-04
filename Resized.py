import cv2

import imutils #Resize

img = cv2.imread('new.png')

resizedImg = imutils.resize(img, width=100)

cv2.imshow('originalImage2.jpg', img)
cv2.imshow('Resized.jpg', resizedImg)

cv2.imwrite('resizedImage2.jpg', resizedImg)
