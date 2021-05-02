#!/usr/bin/env python3

# import
from usrosint.modules.entertainment.dailymotion import Dailymotion
from usrosint.modules.entertainment.vimeo import Vimeo

# daily motion
def dailymotion(self):
    self.result["dailymotion"] = Dailymotion(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("dailymotion")

# vimeo
def vimeo(self):
    self.result["vimeo"] = Vimeo(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("vimeo")