# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:13:05 2020

@author: Supriyo
"""

'''
how to calculate the RGB of an image
'''
import numpy as np
from PIL import Image as img
# im=img.open('test1.png')

# rgb_im=im.convert('RGB')
# r,g,b=rgb_im.getpixel((150,1)) # x and y axis value
# print(r,g,b)

arr=np.zeros([200,200,3],dtype=np.uint8)
arr[:100,:]=[255,0,0]
arr[100:,:]=[0,0,255]
imgd=img.fromarray(arr)
imgd.save('my_img.png')