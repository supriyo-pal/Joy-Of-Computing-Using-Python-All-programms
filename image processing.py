# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:35:12 2020

@author: Supriyo
"""

#flipping the img

from PIL import Image as im

#opening the image
img=im.open('img1.jpg')

#transposing
transposed_img=img.transpose(im.FLIP_LEFT_RIGHT)

#save it to a file in a human understandable format
transposed_img.save('transposed_img.png')
print("Done flipping",transposed_img)