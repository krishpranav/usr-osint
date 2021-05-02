#!/usr/bin/env python3

# imports
from usrosint.modules.domain.domain import Domain

# domain function
def domain(self):
    self.result["domain"] = Domain(self.CONFIG, self.permutations_list).search()
    self.print_results("domain")