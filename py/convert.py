#!/usr/bin/python
# convert image files

import Image
import sys

# arg 1: original 'file.ext', ie. 'photo.jpg'
# arg 2: new 'file.ext', ie. 'photo.png'

im = Image.open(str(sys.argv[1]))
im.save(str(sys.argv[2]))
