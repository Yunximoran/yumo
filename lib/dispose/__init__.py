# vision 视觉
import cv2
import numpy as np


def scaled(ImgObj, resize, isHeight=True):
    """
        图片等比例缩放
    :param ImgObj:
    :param resize:
    :param isHeight:
    :return:
    """
    ih, iw = ImgObj.shape[0], ImgObj.shape[1]
    if isHeight:
        scale = ih / resize
        nw = int(iw / scale)
        NewImgObj = cv2.resize(ImgObj, (nw, resize))
    else:
        scale = iw / resize
        nh = int(ih / scale)
        NewImgObj = cv2.resize(ImgObj, (resize, nh))
    return NewImgObj


if __name__ == '__main__':
    image = cv2.imread("../../material/image/yuanshen.png")

    nimage = scaled(image, 300, True)
    cv2.imshow("scale after image", nimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
