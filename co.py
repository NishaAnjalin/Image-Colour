import cv2
image = cv2.imread("book.png") #Read an image

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', image) #show original

cv2.imshow('Gray',grayImage) #show grayimage

cv2.imwrite('graynew.jpg', grayImage) #save grayimage as jpg


print(image.shape) 

print(image.size)
