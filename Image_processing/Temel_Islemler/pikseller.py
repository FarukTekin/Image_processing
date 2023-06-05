import cv2
import numpy as np

img = cv2.imread("klon.jpg")
color = img[150, 200]
print(color)

Blue = img[150, 200, 0]
print(Blue)

#piksel rengini değiştirme

blue1 = img.item(150, 200, 0)
print("eski", blue1)
img.itemset((150, 200, 0), 172)
print("yeni", img[150, 200, 0] )

print(color)

cv2.waitKey(0)
cv2.destroyAllWindows()