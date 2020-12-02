# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:39:05 2020

@author: Supriyo
"""

import numpy as np
import PIL.Image as p

im=p.open('img2.png')

pixel_map=im.load()

I=np.asanyarray(p.open('img2.png'))

img=p.new(im.mode,im.size)
pixel_new=img.load()

'''
2^8 -> 2^3
2^5=32
 0-31 = 0
 32-36 = 1
 64-95 = 2
 96-127 = 3
 128-159 = 4
 162-191 = 5
 192-223 = 6
 224-255 = 7
'''
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixel_map[i,j]>=0 and pixel_map[i,j]<=31):
                pixel_new[i,j]=0
        
        elif (pixel_map[i,j]>=32 and pixel_map[i,j]<=63):
                pixel_new[i,j]=1
                
        elif (pixel_map[i,j]>=64 and pixel_map[i,j]<=95):
                pixel_new[i,j]=2
                
        elif (pixel_map[i,j]>=96 and pixel_map[i,j]<=127):
                pixel_new[i,j]=3
                
        elif (pixel_map[i,j]>=128 and pixel_map[i,j]<=159):
                pixel_new[i,j]=4
                
        elif (pixel_map[i,j]>=162 and pixel_map[i,j]<=191):
                pixel_new[i,j]=5
                
        elif (pixel_map[i,j]>=192 and pixel_map[i,j]<=223):
                pixel_new[i,j]=6
        
        elif (pixel_map[i,j]>=224 and pixel_map[i,j]<=255):
                pixel_new[i,j]=7
img.save('datacompression.png')
j=np.asanyarray(p.open('datacompression.png'))