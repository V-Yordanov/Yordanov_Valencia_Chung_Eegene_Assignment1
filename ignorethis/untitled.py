import os

here = os.path.dirname(os.path.realpath(__file__))
subdir = "replace"
filename = "replace.txt"
filepath = os.path.join(here, subdir, filename)

# create your subdirectory
os.mkdir(os.path.join(here, subdir))

# create an empty file.
try:
    f = open(filepath, 'w')
    
    f.close()
except IOError:
    print("Wrong path provided")