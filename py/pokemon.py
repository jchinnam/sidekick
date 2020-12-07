#!/usr/bin/python
# a random pokemon says hello
# usage: python pokemon.py

import requests
import random

def request(url, payload):
    response = requests.request("GET", url, data=payload)
    return response.json()

# get total num of pokemon to date
all_pokemon = request("https://pokeapi.co/api/v2/pokedex/national", "")
num_pokemon = len(all_pokemon["pokemon_entries"])

rand_pokemon_id = random.randint(1,num_pokemon - 1)  # from 1 to num_pokemon, inclusive

# get specific pokemon
pokemon = request("http://pokeapi.co/api/v2/pokemon/" + str(rand_pokemon_id) + "/", "")
name = pokemon["forms"][0]["name"]

print(name + " says hello")
