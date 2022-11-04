# Name         : Waseem Alkasbutrus
# ID           : 1001849127
# Lang Version : Python 2.7.18
# OS           : Ubuntu 20.04.5 LTS (Not on a virtual machine)

# NOTE: Check README.md for answer to questions 1 and 2

import os

def sumFileSizes(dir):
    size = 0

    # get entries of dir
    entries = os.listdir(dir)

    # for each object in the current directory
    for entry in entries:

        # combine file/ directory name with current path to correctly read files/dirs in subdirectories
        fullEntry = os.path.join(dir, entry)

        # check if it is a file or a directory
        if os.path.isfile(fullEntry):
            # if it is a file, get its size
            size += os.path.getsize(fullEntry)
        elif os.path.isdir(fullEntry):
            # if it is a dir, call this function again
            size += sumFileSizes(fullEntry)
    
    return size

sum = sumFileSizes(os.getcwd())
print(sum)