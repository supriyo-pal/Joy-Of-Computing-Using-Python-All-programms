# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:24:27 2020

@author: Supriyo
"""

'''
An image contains of matrix of pixels.A pixel is basically a color.
A color is defined by 3 attribures, 
Red,blue and green
'''

import numpy as np
from PIL import Image

width=555
height=455

array=np.zeros([height,width,3],dtype=np.uint8)
img=Image.fromarray(array)
img.save('test.png')

array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0]#orange
array1[:,100:]=[0,0,255]#blue
img=Image.fromarray(array1)
img.save("test1.png")







