#!/usr/bin/python
# look for available usernames
# usage: python reddit_user.py [optional arg1 for a specific username]

import requests
import json
import sys
import re
import itertools

illegal = re.compile(r"[<>/{}[\]~,.!@#$%^&*()`']")
username = ""

def has_illegal_chars(word):
    return illegal.search(word)

# if checking a specific username
if (len(sys.argv) == 2):
    username = sys.argv[1]
    url = "https://www.reddit.com/api/username_available.json?user=" + str(username)

    # make reddit api call
    # use a valid existing account username for the header
    response = requests.request("GET", url, headers={'User-Agent': 'INSERT_SOME_VALID_USERNAME'})
    data = response.json()

    if (data):
        print(str(username) + " is available")
    else:
        print(str(username) + " is not available")

    exit(0)

# else, checking for currently available dictionary word reddit usernames
# set repeat to length of username (i.e. 4 produces 4-char usernames)
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
keywords = [''.join(i) for i in itertools.product(chars, repeat = 4)]

# read in list of dictionary words
github_response = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt")
word_list = github_response.text.splitlines()

for word in word_list:

    # filter out if illegal chars or < 3 chars
    if (len(word) < 3 or has_illegal_chars(word)):
        continue

    url = "https://www.reddit.com/api/username_available.json?user=" + str(word)

    # make reddit api calls
    response = requests.request("GET", url, headers={'User-Agent': 'INSERT_SOME_VALID_USERNAME'})
    data = response.json()

    if (data):
        print(word)
