import os
import errno
from math import *
import numpy as np
from scipy import *
import shutil
 
def name_find_replace(name,find,replace):
    '''
    This function finds a file called 'name', and finds a word called find, and
    replaces it with replace. Then it creates a new file with the replaced word
    
    When calling this function make sure to add spaces before and after the 
    find and replace strings, so that the words are separated by a space
    '''
    
    open_file = open(name, 'r') # open the file we want to replace
    contents = open_file.read() # 'str': read the contents of this file
    contents = contents.replace(find,replace) # replacae the word 'find' with 'replace'

    here = os.path.dirname(os.path.realpath(__file__)) # current directory
    subdir = "replace" # new subdirectory, ie. our file name
    filename = "replace.txt" # our new file name
    filepath = os.path.join(here, subdir, filename) # create path to file

    # create subdirectory
    os.mkdir(os.path.join(here, subdir))
    # create an file
    f = open(filepath, 'w') # open the new file
    f.write(contents) # write to the new file
    f.close() # close the file

        
print("BEFORE YOU START, MAKE SURE THE FOLDER AND FILE 'replace' DOESN'T ALREADY EXIST IN YOUR DIRECTORY")
name_find_replace('testparagraph2.txt', ' Bob ', ' a cat ')