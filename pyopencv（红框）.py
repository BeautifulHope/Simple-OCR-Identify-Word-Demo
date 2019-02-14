#!/usr/bin/env python3
# -*- coding: utf-8 -*

import cv2
import numpy as np
from collections import deque

# #读取图像，支持 bmp、jpg、png、tiff 等常用格式
# img = cv2.imread("test_1.jpg")

#转化为灰度
# gray = cv2..cv2.Color(img, cv2..COLOR_BGR2GRAY)

# gradX = cv2..Sobel(gray, ddepth=cv2..cv2.32F, dx=1, dy=0, ksize=-1)
# gradY = cv2..Sobel(gray, ddepth=cv2..cv2.32F, dx=0, dy=1, ksize=-1)
#
# # subtract the y-gradient from the x-gradient
# gradient = cv2..subtract(gradX, gradY)
# gradient = cv2..convertScaleAbs(gradient)
#
# blurred = cv2..blur(gradient, (9, 9))
# cv2..threshold(blurred, 90, 255, cv2..THRESH_BINARY)
#
# cv2..imshow("image",gray)
# cv2..waitKey(0)
# cv2..destroyAllWindows()
#


#设定红色阈值，HSV空间
import time

greenLower = np.array([35, 43, 46])
greenUpper = np.array([77, 255, 255])
#设定绿色阈值，HSV空间

redLower = np.array([0, 0, 254])
redUpper = np.array([0, 0, 255])
#设定红色阈值，HSV空间


#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread("test_1.jpg")
img_2 = cv2.imread("test_1.jpg")

#图片转化为hsv数据
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 根据阈值构建掩膜
mask = cv2.inRange(hsv, greenLower, greenUpper)

(_,cnts,_) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    # cv2.drawContours(img, [box], 0, (0, 255, 0), 6)
    # cv2.drawContours(img,[box],-1,(151,210,172),thickness=-1)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1
    cv2.rectangle(img, (x1, y2), (x2, y1), (0, 0, 255), 2)

cv2.imshow("Image1",img)
cv2.imwrite("C:\\Users\L1308\Desktop\Python Demo\project\image\\test2\outcome_img.jpg", img)

#############选取红框###################
hsv_r = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 根据阈值构建掩膜
mask_r = cv2.inRange(hsv, redLower, redUpper)
(_,rcnts,_) = cv2.findContours(mask_r, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for rcnt in rcnts:

    r_rect = cv2.minAreaRect(rcnt)
    box = cv2.boxPoints(r_rect)
    box = np.int0(box)
    cv2.drawContours(img_2,[box],-1,(0,0,0),thickness=-1)

cv2.imshow("Image2",img)
# res = cv2.bitwise_and(img,img,mask=mask)
# gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

#创建窗口并显示图像
# cv2.namedWindow("Image")
cv2.imshow("mask_2",mask_r)
# cv2.imshow("img_2",img_2)
# cv2.imshow("res_2",res_2)
# cv2.imshow("Gray_2",gray)

# cv2.imwrite("C:\\Users\L1308\Desktop\Python Demo\project\image\\test2\outcome_gray_2.jpg", gray)
# cv2.imwrite("C:\\Users\L1308\Desktop\Python Demo\project\image\\test2\outcome_mask_2.jpg", mask)
# cv2.imwrite("C:\\Users\L1308\Desktop\Python Demo\project\image\\test2\outcome_res_2.jpg", res)

cv2.waitKey(0)

#释放窗口
cv2.destroyAllWindows()