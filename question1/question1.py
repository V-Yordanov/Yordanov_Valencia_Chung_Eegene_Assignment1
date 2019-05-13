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
    
    

name_find_replace('testparagraph2.txt', ' Bob ', ' a cat ')



def createDir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
createDir('./replace/')
#
#
#
#filename = "replace.txt"
#os.makedirs(os.path.dirname(''), exist_ok=True)
#with open(filename, "w+") as f:
#    f.write("replace.txt")
#
#'c:/your/full/path'

name_find_replacef = open(Yordanov_Valencia_Chung_Eegene_Assignment1/question1/replace, "a")

    