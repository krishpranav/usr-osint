#!/usr/bin/env python3

# imports
import requests
import time

class Domain:

    def __init__(self, config, permutations_list):
        self.delay = config['plateform']['domain']['rate_limit'] / 1000
        self.format = config['plateform']['domain']['format']
        self.tld = config['plateform']['domain']['TLD']
        self.permutations_list = [perm.lower() for perm in permutations_list]
        self.type = config['plateform']['domain']['type']
        
    def possible_domains(self):
        possible_domains = []

        for domain in self.tld:
            for permutation in self.permutations_list:
                possible_domains.append(self.format.format(
                    permutation = permutation,
                    domain = domain
                ))

        return possible_domains
    
    def search(self):
        domains_list = {
            "type": self.type,
            "accounts": []
        }
        possible_domains_list = self.possible_domains()

        for domain in possible_domains_list:
            try:
                r = requests.head(domain, timeout=5)
            except requests.ConnectionError:
                pass
                
            if r.status_code < 400:
                domains_list ["accounts"].append({"value": domain})
            time.sleep(self.delay)
        
        return domains_list