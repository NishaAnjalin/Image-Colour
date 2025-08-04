import cv2
img = cv2.imread("book.png") #Read an image

cv2.imshow('Show', img) #To display the image

cv2.imwrite('Harry.jpg', img) #To save the image

cv2.waitKey(5000)
cv2.destroyAllWindows()

