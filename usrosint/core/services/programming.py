#!/usr/bin/env python3

# imports
from usrosint.modules.programming.github import Github
from usrosint.modules.programming.pastebin import Pastebin
from usrosint.modules.programming.replit import Replit

# github
def github(self):
    self.result["github"] = Github(self.CONFIG, self.permutations_list).search()
    self.print_results("github")

# pastebin
def pastebin(self):
    self.result["pastebin"] = Pastebin(self.CONFIG, self.permutations_list).search() 
    self.print_results("pastebin")

# Repl.it
def replit(self):
    self.result["replit"] = Replit(self.CONFIG, self.permutations_list).search() 
    self.print_results("replit")