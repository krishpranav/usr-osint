#!/usr/bin/env python3
# logo file 

from usrosint.core.colors import Colors

def print_logo(self):
    print(Colors.OKGREEN + Colors.BOLD + '''
        usr-osint
''' + Colors.ENDC)
    
    print(Colors.HEADER + "Version {version} - Developped by krishpranav".format(version=self.version))