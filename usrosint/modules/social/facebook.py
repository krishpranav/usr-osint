#!/usr/bin/env python3

# imports
import requests
import time

class Facebook:

    def __init__(self, config, permutations_list):
        self.delay = config['plateform']['facebook']['rate_limit'] / 1000
        self.format = config['plateform']['facebook']['format']
        self.permutations_list = [perm.lower() for perm in permutations_list]
        self.type = config['plateform']['facebook']['type']

    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        facebook_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to facebook")
            
            if r.status_code == 200:
                facebook_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return facebook_usernames