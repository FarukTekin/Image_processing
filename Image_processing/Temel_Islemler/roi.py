import cv2
import numpy as np

#roi --> region of iterest(ilgi alanı)

img = cv2.imread("klon.jpg")
#print(img.shape[:2])

roi = img[30:190, 200:375]
cv2.imshow("roi", roi)
cv2.imshow("klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()