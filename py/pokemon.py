#!/usr/bin/python
# a random pokemon says hello

import requests
import random

rand_pokemon_id = random.randint(1,721)  # from 1 to 720, inclusive

url = "http://pokeapi.co/api/v2/pokemon/" + str(rand_pokemon_id) + "/"

payload = ""
response = requests.request("GET", url, data=payload)
data = response.json()

name = data["forms"][0]["name"]

print(name + " says hello")
