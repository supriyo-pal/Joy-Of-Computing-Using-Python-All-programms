# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:52:46 2020

@author: Supriyo
"""
#image enhancement CLAHE
import cv2
import numpy as np
img=cv2.imread('img2.png')

#preparation for CLAHE
clahe=cv2.createCLAHE()

#convert it into grey scale image
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#apply enhancement
enh_img=clahe.apply(gray_image)

#saving the file
cv2.imwrite("enhanced_image.png",enh_img)
print("done enhancing")