import cv2
img = cv2.imread('new.png')

#dst = cv2. GassianBlur(src, (kernel), borderType)

gaussianImg = cv2.GaussianBlur(img, (41,41), 50) #smooth

gaussianImg1 = cv2.GaussianBlur(img, (21,21), 0)

cv2.imshow("Original", img)
cv2.imshow("GaussianBlur", gaussianImg)
cv2.imshow("GaussianBlur1", gaussianImg)
