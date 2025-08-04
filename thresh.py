import cv2

img=cv2.imread("new.png")

grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#dst=cv2.threshold(src,threshold, maxValueForThreshold,binary,type)[1]

thresholdImg = cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY)[0]
print(thresholdImg)

#thresholdImg = cv2.threshold(grayImg,100,255,cv2.THRESH_BINARY)[1]

#thresholdImg = cv2.threshold(grayImg,160,255,cv2.THRESH_BINARY)[1]

thresholdImg = cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY)[1]

cv2.imshow("Original", img)

cv2.imshow("threshold.jpg", thresholdImg)

#0-Black
#180-
#255-White
