import cv2
import numpy as np

image = cv2.imread("image\\yuanshen.png")

# data = image[image > 100] = 0

_, threshold_img = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
# thresh_binary - 二值化
size = 600

h, w = threshold_img.shape[0], threshold_img.shape[1]

scale = h / size
nw = int(w / scale)

threshold_img = cv2.resize(threshold_img, (nw, 600))
print(threshold_img)  # 二值 0 | 255

cv2.imshow("d", threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
