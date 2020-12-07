#!/usr/bin/python
# convert image files
# usage: python image.py file.ext1 file.ext2
# i.e. python image.py photo.jpg photo.png (where jpg is the original and png is the goal)

import Image
import sys

im = Image.open(str(sys.argv[1]))
im.save(str(sys.argv[2]))
