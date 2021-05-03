#!/usr/bin/env python3

# imports
from usrosint.modules.music.soundcloud import Soundcloud
from usrosint.modules.music.spotify import Spotify

# sound cloud
def soundcloud(self):
    self.result["soundcloud"] = Soundcloud(self.CONFIG, self.permutations_list).search()
    self.print_results("soundcloud")

# spotify
def spotify(self):
    self.result["spotify"] = Spotify(self.CONFIG, self.permutations_list).search()
    self.print_results("spotify")
