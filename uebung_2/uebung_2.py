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
    global drawr, xi,yi,img
    if event == cv2.EVENT_LBUTTONDOWN:
        xi,yi = x,y
        drawr = True
    if event == cv2.EVENT_MOUSEMOVE:
        if drawr == True:
            img = orig.copy()
            cv2.rectangle(img,(xi,yi),(x,y),(0,0,0),2)        
    if event == cv2.EVENT_LBUTTONUP:
        if drawr == True:
            img = orig.copy()
            
            print("xi=",xi,"yi=",yi)
            print("x=",x,"y=",y)
            
            if xi<x and yi<y:
                img_crop = orig[yi:y,xi:x]
            if xi>x and yi>y:
                img_crop = orig[y:yi,x:xi]
            if xi<x and yi>y:
                img_crop = orig[y:yi,xi:x]
            if xi>x and yi<y:
                img_crop = orig[yi:y,x:xi]
                
                
                
            print(img_crop.shape)
            
            img_zoom = cv2.resize(img_crop,fx=2,fy=2,dsize=(0,0))
            cv2.imshow("img_zoom",img_zoom)
            
            cv2.rectangle(img,(xi,yi),(x,y),(0,0,0),2)
            drawr = False

        

drawr = False
(xi,yi)=(0,0)
while True:
    cv2.imshow("img", img)
    cv2.setMouseCallback('img',draw)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()