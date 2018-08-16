#!/usr/bin/python
# google something

import webbrowser
import sys

query = ""

for i in range(1, len(sys.argv)):
    query += " "
    query += sys.argv[i]

url = "https://www.google.com/search?q={}".format(query)

b = webbrowser.get('safari')
b.open(url)
