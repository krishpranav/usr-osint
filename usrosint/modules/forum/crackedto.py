#!/usr/bin/env python3

# imports
import requests
import time

class CrackedTo:

    def __init__(self, config, permutations_list):
        self.delay = config['plateform']['crackedto']['rate_limit'] / 1000
        self.format = config['plateform']['crackedto']['format']
        self.permutations_list = permutations_list
        self.type = config['plateform']['crackedto']['type']

    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        cracked_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to cracked.to")
            
            if r.status_code == 200:
                cracked_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return cracked_usernames