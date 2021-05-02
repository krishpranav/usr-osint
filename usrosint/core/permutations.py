#!/usr/bin/env python3

# import
from itertools import chain, combinations, permutations

# get permutationns self 
def get_permutations(self):
    [self.items.append(separator) for separator in self.separators]

    combinations_list = list(chain(*map(lambda x: combinations(self.items, x), range(1, len(self.items) + 1))))   
    for combination in combinations_list:
        for perm in list(permutations(combination)):
            consecutives_separators = False in [(not perm[i] in self.separators) or (not perm[i + 1] in self.separators) for i in range(len(perm) - 1)]
            
            if not perm[0] in self.separators and not perm[-1] in self.separators and not consecutives_separators:
                self.permutations_list.append("".join(perm))