#!/usr/bin/env python3

# import
from usrosint.modules.money.bymeacoffee import BuyMeACoffee

# bymeacoffee
def buymeacoffee(self):
    self.result["buymeacoffee"] = BuyMeACoffee(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("buymeacoffee")