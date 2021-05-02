#!/usr/bin/env python3

# import
from usrosint.modules.email.email import Email

def email(self):
    self.result["email"] = Email(self.CONFIG, self.permutations_list).search()
    self.print_results("emails")