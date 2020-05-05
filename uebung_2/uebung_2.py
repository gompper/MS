# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:45:00 2020

@author: urs
"""

import cv2
#import numpy as np

orig = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE) # 0 = Greyscale

img = orig.copy()
    

def draw(event,x,y,flags,parm):
    global drawr, start_pt,img
    if event == cv2.EVENT_LBUTTONDOWN:
        start_pt = x,y
        drawr = True
    if event == cv2.EVENT_MOUSEMOVE:
        if drawr == True:
            img = orig.copy()
            cv2.rectangle(img,start_pt,(x,y),(0,0,0),2)        
    if event == cv2.EVENT_LBUTTONUP:
        drawr = False
        if drawr == True:
            end_pt = x,y
            cv2.rectangle(img,start_pt,end_pt,(0,0,0),2)

        

drawr = False
start_pt = 0,0
while True:
    cv2.imshow("img", img)
    cv2.setMouseCallback('img',draw)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
# Show image
#cv2.imshow('image',img)
#cv2.waitKey(0)
cv2.destroyAllWindows()