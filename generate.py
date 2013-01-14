#!/usr/bin/python
# This application is a hack (For now)
# All I want it to accomplish is to generate a static version
# of ArthikTangi.com (literally translates to, 'Financial Strain')

__version__ = "0.0.1"

import os
import sys
import time
import shutil

from readers import csvreader
from writers import staticwriter

from settings import get_settings

class Comatic:
    def __init__(self, settings):
        """
        Do some initialization stuff here
        """
        self.output_path = settings['OUTPUT_PATH']
        self.settings = settings
        
    def output_folder_ready(self, outdir):
        """
        Ask to remove the output folder if it exists
        """
        if os.path.isdir(outdir) is False:
            return True
        else:
            response = raw_input('CAUTION! Read file path carefully.\nThe path "%s" already exists. Remove? (y/n)' % outdir)
            if response is 'y' or response is 'Y':
                #remove directory
                shutil.rmtree(outdir)
                return True
            else:
                return False
            

    def init_path(self):
        if not any(p in sys.path for p in ['', '.']):
            sys.path.insert(0, '')
            
    def copy_static_files(self):
        output_root = os.path.abspath(os.path.expanduser(self.settings['OUTPUT_PATH']))
        if (self.output_folder_ready(output_root)):
            for folder in self.settings['STATIC']:
                destpath = os.path.join(self.settings['OUTPUT_PATH'], 'static')
                staticwriter(os.path.abspath(os.path.expanduser(folder)),
                             os.path.abspath(os.path.expanduser(destpath)))
        else:
            print "Copying static files failed"
        # Read the comic details


    def run(self):
        """
        copy static files.
        read comic csv.
        write comics.
        rejoice.
        """
        # copying static files
        self.copy_static_files()

        #read comic CSV
        csvreader(os.path.abspath(os.path.expanduser(self.settings['COMIC_CSV'])))
        print "Done"


def main():
    settings = get_settings()
    comatic = Comatic(settings)
    comatic.init_path()
    comatic.run()


if __name__ == "__main__":
    main()
