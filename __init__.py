# This application is a hack (For now)
# All I want it to accomplish is to generate a static version
# of ArthikTangi.com (literally translates to, 'Financial Strain')

__version__ = "0.0.1"

import time

from pelican.readers import comicreader
from pelican.writers import comicgenerator

from pelican.settings import get_settings

class Comatic(object):
    def __init__(self, settings):
        """
        Do some initialization stuff here
        """
        self.output_path = settings['OUTPUT_PATH']
        self.
        
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

