#!/usr/bin/env python3

# imports
from usrosint.modules.forum.zeroxzerozerosec import ZeroxZeroZeroSec
from usrosint.modules.forum.jeuxvideo import JeuxVideo
from usrosint.modules.forum.hackernews import Hackernews
from usrosint.modules.forum.crackedto import CrackedTo

def zeroxzerozerosec(self):
    self.result["0x00sec"] = ZeroxZeroZeroSec(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("0x00sec")

# jeuxvideo.com
def jeuxvideo(self):
    self.result["jeuxvideo.com"] = JeuxVideo(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("jeuxvideo.com")

# hackernews
def hackernews(self):
    self.result["hackernews"] = Hackernews(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("hackernews")

# Cracked.to
def crackedto(self):
    self.result["crackedto"] = CrackedTo(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("crackedto")