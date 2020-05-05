# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:02:14 2020

@author: urs
"""

import cv2
import numpy as np

width = 600
height = 600

# Create a black image
img = np.zeros((width,height,3), np.uint8)

# Make image grey
img[:,:] = (92,92,92)      # (B, G, R)

# Add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Test',(300,300), font, 2,(0,255,0),2,cv2.LINE_AA)

# Rotate image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Show image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()