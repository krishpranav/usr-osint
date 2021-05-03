#!/usr/bin/env python3

# imports
import time
import pwnedpasswords

class Email:
    
    def __init__(self, config, permutations_list):
        self.delay = DELAY = config['plateform']['email']['rate_limit'] / 1000
        self.domains = config['plateform']['email']['domains']
        self.format = config['plateform']['email']['format']
        self.permutations_list = [perm.lower() for perm in permutations_list]
        self.type = config['plateform']['email']['type']

    def possible_emails(self):
        possible_emails = []

        for domain in self.domains:
            for permutation in self.permutations_list:
                possible_emails.append(self.format.format(
                    permutation = permutation,
                    domain      = domain
                ))
        return possible_emails

    def search(self):
        emails_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_emails_list = self.possible_emails()

        for possible_email in possible_emails_list:
            pwned = pwnedpasswords.check(possible_email)

            if not pwned:
                emails_usernames["accounts"].append({"value": possible_email, "breached": False})
            else:
                emails_usernames["accounts"].append({"value": possible_email, "breached": True})

            time.sleep(self.delay)

        return emails_usernames