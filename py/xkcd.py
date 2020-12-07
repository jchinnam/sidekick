#!/usr/bin/python
# grab & open today's xkcd comic
# usage: python xkcd.py

from PIL import Image
import urllib.request as req
import json
import os

response = req.urlopen("https://xkcd.com/info.0.json")

obj = json.loads(response.read())

# print comic info
print("Comic #" + str(obj["num"]))
print(obj["alt"])

# show comic
req.urlretrieve(obj["img"], "temp.jpg")
img = Image.open('temp.jpg')
img.show()
os.remove('temp.jpg')
