import cv2
import numpy as np

img = cv2.imread("klon.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("klon",img)
cv2.imshow("klonRGB", img_rgb)
cv2.imshow("klonHSV", img_hsv)
cv2.imshow("klonGRAY", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows