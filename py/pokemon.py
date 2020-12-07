#!/usr/bin/python
# a random pokemon says hello

import requests
import random

# get total num of pokemon to date
url = "https://pokeapi.co/api/v2/pokedex/national"

payload = ""
response = requests.request("GET", url, data=payload)
all_pokemon = response.json()

num_pokemon = len(all_pokemon["pokemon_entries"])

rand_pokemon_id = random.randint(1,num_pokemon - 1)  # from 1 to num_pokemon, inclusive

url = "http://pokeapi.co/api/v2/pokemon/" + str(rand_pokemon_id) + "/"

payload = ""
response = requests.request("GET", url, data=payload)
data = response.json()

name = data["forms"][0]["name"]

print(name + " says hello")
