#!/usr/bin/env python3

# imports
import requests
import time

class Twitter:

    def __init__(self, config, permutations_list):
        self.delay = config['plateform']['tiktok']['rate_limit'] / 1000
        self.format = config['plateform']['twitter']['format']
        self.permutations_list = permutations_list

        self.nitter_URL = [
            "https://nitter.42l.fr/{}",
            "https://nitter.pussthecat.org/{}",
            "https://nitter.nixnet.services/{}",
            "https://nitter.tedomum.net/{}",
            "https://nitter.fdn.fr/{}",
            "https://nitter.kavin.rocks/{}",
            "https://tweet.lambda.dance/{}"
        ]

        #social
        self.type = config['plateform']['twitter']['type']

    # Generate all potential twitter usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    # Return a working nitter instance
    def get_nitter_instance(self):
        for nitter_instance in self.nitter_URL:
            if requests.get(nitter_instance.format("pewdiepie")).status_code == 200:
                return nitter_instance

    def search(self):
        twitter_usernames = {
            "type": self.type,
            "accounts" : []
        }

        nitter_URL = self.get_nitter_instance()

        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                nitter_formatted_URL = nitter_URL.format(username.replace("https://twitter.com/", ""))
                r = requests.get(nitter_formatted_URL)
            except requests.ConnectionError:
                print("failed to connect to twitter")
            
            if r.status_code == 200:
                twitter_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)

        return twitter_usernames