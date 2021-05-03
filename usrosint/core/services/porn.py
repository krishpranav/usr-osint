#!/usr/bin/env python3

# imports
from usrosint.modules.porn.pornhub import Pornhub
from usrosint.modules.porn.redtube import Redtube

# porn hub
def pornhub(self):
    self.result["pornhub"] = Pornhub(self.CONFIG, self.permutations_list).search()
    self.print_results("pornhub")

# red tube
def redtube(self):
    self.result["redtube"] = Redtube(self.CONFIG, self.permutations_list).search()
    self.print_results("redtube")
