#!/usr/bin/python
# google something
# usage: python google.py [search query]
# i.e. python google.py pizza near me

import webbrowser
import sys

query = ""

for i in range(1, len(sys.argv)):
    query += " "
    query += sys.argv[i]

url = "https://www.google.com/search?q={}".format(query)

b = webbrowser.get('safari')
b.open(url)
