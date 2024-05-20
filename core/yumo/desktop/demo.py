import cv2
import threading

import cv2

# 创建一个窗口，窗口名称为"Image"
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# 读取一张图片
img = cv2.imread("image/preview.jpg")

while True:
    # 在窗口中显示图片
    cv2.imshow("Image", img)

    # 等待1ms，如果期间按下q键，则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 销毁所有窗口
cv2.destroyAllWindows()


# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# # 原始图像读取
# image = cv2.imread("image\\preview.jpg")
# # 输入你想要resize的图像高。
# size = 640
# # 获取原始图像宽高。
# height, width = image.shape[0], image.shape[1]
# # 等比例缩放尺度。
# scale = height/size
# # 获得相应等比例的图像宽度。
# width_size = int(width/scale)
# # resize
# image_resize = cv2.resize(image, (width_size, size))
#
# cv2.imshow('ir', image_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
