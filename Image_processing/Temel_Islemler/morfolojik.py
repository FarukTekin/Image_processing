import cv2
import numpy as np

img = cv2.imread("Turk.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
#erosion = cv2.erode(img, kernel, iterations = 2) siyahlıklar artıyor
#dilation = cv2.dilate(img, kernel, iterations = 5) #beyazlıklar artıyor
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #tüm gürültü silme
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) #nesnenin içindeki bozulmalar silinir
#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) #nesnenin iiçini siyah bırakır
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) # nesnenin bazı noktalarını siyahlaştırır
#black hat yöntemide var

cv2.imshow("tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()