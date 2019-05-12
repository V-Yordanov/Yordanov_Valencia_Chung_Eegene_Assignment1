# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:28:23 2019

@author: User
"""

from math import *
import numpy as np
from scipy import *

    
def name_find_replace(name,find,replace):
    '''
    This function finds a file called 'name', and finds a word called find, and
    replaces it with replace. Then it creates a new file with the replaced word
    
    When calling this function make sure to add spaces before and after the 
    find and replace strings, so that the words are separated by a space
    '''

    open_file = open(name, 'r')
    contents = open_file.read()
    
    newfile = open('replace.txt', 'w+')
    contents = contents.replace(find,replace)
    newfile.write(contents)




name_find_replace('testparagraph.txt', ' is ', ' cats ')











##Okay, so far I've been able to make python discern words, and match the word I
##want to the word in the file.
#f = open('testparagraph.txt')
#for word in f.read().split():
#    if word == find:
#        word = replace
#        print('Match')
#    else:
#        print('Not Match')


    #print(contents)
    
    #find = ' is '
    
    #replace = 'zyzyzyz'










    