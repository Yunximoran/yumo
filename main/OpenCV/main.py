import cv2

window_name = 'yumo'
window_width = 640
window_height = 480

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, window_width, window_height)

img = cv2.imread('material/image/yuanshen.png')

print(img[0])
print(img[1])
print(img[2])

cv2.imshow(window_name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
