import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = np.zeros((500, 500), np.uint8) +50
#cv2.rectangle(img, (0, 60), (200, 150), (255, 255, 255), -1)
#cv2.rectangle(img, (250, 170), (350, 200), (255, 255, 255), -1)

img1 = cv2.imread("klon.jpg")
b, g, r = cv2.split(img1)

cv2.imshow("img", img1)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()