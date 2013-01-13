#!/usr/bin/python
# This application is a hack (For now)
# All I want it to accomplish is to generate a static version
# of ArthikTangi.com (literally translates to, 'Financial Strain')

__version__ = "0.0.1"

import os
import sys
import time

#from pelican.readers import comicreader
#from pelican.writers import comicgenerator

from settings import get_settings

class Comatic:
    def __init__(self, settings):
        """
        Do some initialization stuff here
        """
        self.output_path = settings['OUTPUT_PATH']
        
    def init_path(self):
        if not any(p in sys.path for p in ['', '.']):
            sys.path.insert(0, '')

    def run(self):
        """
        copy static files.
        read comic rst.
        write comics.
        rejoice.
        """
        print "Hurrah!"


def main():
    settings = get_settings()
    comatic = Comatic(settings)
    comatic.init_path()
    comatic.run()


if __name__ == "__main__":
    main()
