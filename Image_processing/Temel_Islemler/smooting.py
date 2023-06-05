import cv2
import numpy as np

img_filter = cv2.imread("klon.jpg")
img_median = cv2.imread("C:\\Users\\omer9\\Desktop\\erwin.jpg")
img_bilateral = cv2.imread("Turk.jpg")

blur = cv2.blur(img_filter, (5,5))
blur2 = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median, 9)
blur_b = cv2.bilateralFilter(img_bilateral, 9, 95, 95)

cv2.imshow("original", img_bilateral)
#cv2.imshow("blur", blur)
#cv2.imshow("blur2", blur2)
#cv2.imshow("blur_m", blur_m)
cv2.imshow("bilateral", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()

