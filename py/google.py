#!/usr/bin/python
# google something

import webbrowser
import sys

search_phrase = ""
for i in range(1, len(sys.argv)):
	search_phrase += " "
	search_phrase += sys.argv[i]

url = "https://www.google.com/search?q={}".format(search_phrase) 
b = webbrowser.get('safari')
b.open(url)