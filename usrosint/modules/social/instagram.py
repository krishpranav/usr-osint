#!/usr/bin/env python3

# imports
import requests
import time

class Instagram:

    def __init__(self, config, permutations_list):
        self.delay = config['plateform']['instagram']['rate_limit'] / 1000
        self.format = config['plateform']['instagram']['format']
        self.permutations_list = permutations_list
        self.type = config['plateform']['instagram']['type']

    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        instagram_usernames = {
            "type": self.type,
            "accounts" : []
        }

        bibliogram_URL = "https://bibliogram.art/u/{}"

        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                bibliogram_formatted_URL = bibliogram_URL.format(username.replace("https://instagram.com/", ""))
                r = requests.get(bibliogram_formatted_URL)
            except requests.ConnectionError:
                print("failed to connect to instagram")
            
            if r.status_code == 200:
                instagram_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return instagram_usernames