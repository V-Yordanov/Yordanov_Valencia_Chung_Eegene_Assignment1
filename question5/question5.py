# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:31:17 2019

@author: User
"""
import numpy as np
from math import *
from PIL import Image, ImageDraw



def mandelbrot(c,iterations):
    '''
    This function iterates the z complex value. The general formula is:
    z = z^2 + c, where c can be complex as well. It outputs the number of
    iterations done before the value diverges outside of the boundary of 
    |z|^2<=2
    '''
    z = 0
    n = 0
    while abs(z) <= 2 and n < iterations:
        z = z**2 + c
        n += 1
    return n



def colour_pixels(m,iterations):
    '''
    This function takes in the m value, and the iteration of the pixel, and
    outputs it's colour, based on its iteration number
    '''
    hue = (255*m//iterations)
    saturation = 255
    if m < iterations:
        value = 255
    else:
        value = 0
    return hue,saturation,value
    
    

def mandelbrot_fractal(iterations,image_width,image_height):
    '''
    This function plots the mandelbrot set.
    '''
    #The mode HSV used here is hue, saturation, and color
    im = Image.new('HSV', (image_width, image_height), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    
    # Plot window
    Re_start = -2
    Im_start = -1
    Re_end = 1
    Im_end = 1
    Re_size = Re_end - Re_start
    Im_size = Im_end - Im_start
    

    for x in np.arange(0, image_width, 0.5):
        for y in np.arange(0, image_height, 0.5):
            

            re_x = Re_start + (x/image_width) * (Re_size)
            im_y = Im_start + (y/image_height) * (Im_size)
            
            c = complex(re_x, im_y)
            
            m = mandelbrot(c,iterations)
            hue, saturation, value = colour_pixels(m,iterations)
            draw.point([x, y], (hue, saturation, value))
    
    return im.show()
    

mandelbrot_fractal(100,600,400)








#im.convert('RGB').save('mandelbrot_fractal.png', 'PNG')

