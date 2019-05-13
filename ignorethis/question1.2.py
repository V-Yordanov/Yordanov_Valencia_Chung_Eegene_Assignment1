# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:28:23 2019

@author: User
"""
import os
import errno
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
    
    




#def createDir(directory):
#    try:
#        if not os.path.exists(directory):
#            os.makedirs(directory)
#    except OSError:
#        print ('Error: Creating directory. ' +  directory)
#        
#createDir('./replace/')

def name_find_replace(name,find,replace):
    
    open_file = open(name, 'r')
    contents = open_file.read()
    
    newfile = open('replace.txt', 'w+')
    contents = contents.replace(find,replace)
    newfile.write(contents)
    

    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "replace"
    filename = "replace.txt"
    filepath = os.path.join(here, subdir, filename)
    
    # create your subdirectory
    os.mkdir(os.path.join(here, subdir))
    
    # create an empty file.
    try:
        f = open(filepath, 'w')
        f.write(contents)
        f.close()
    except IOError:
        print("Wrong path provided")





name_find_replace('testparagraph2.txt', ' Bob ', ' a cat ')







    