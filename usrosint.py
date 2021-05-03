#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import sys
from itertools import chain, combinations
from usrosint.core import Core
from usrosint.core.colors import Colors
from multiprocessing import Process

CONFIG = './config.json'

profil3r = Core(CONFIG).run()