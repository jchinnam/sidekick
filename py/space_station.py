#!/usr/bin/python
# print current location of the international space station

import urllib.request as request
import json

response = request.urlopen("http://api.open-notify.org/iss-now.json")

obj = json.loads(response.read())

latitude = obj['iss_position']['latitude']
longitude = obj['iss_position']['longitude']

print(str(obj['timestamp']) + ' : ' + latitude + ' , ' + longitude)
