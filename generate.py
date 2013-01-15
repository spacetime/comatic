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
from writers import defaultwriter

from settings import get_settings

class Comatic:
    def __init__(self, settings):
        """
        Do some initialization stuff here
        """
        self.output_path = settings['OUTPUT_PATH']
        self.settings = settings
        self.output_root = os.path.abspath(os.path.expanduser(self.settings['OUTPUT_PATH']))
        self.destpath = os.path.join(self.settings['OUTPUT_PATH'], 'static')
        self.themepath = os.path.join( 'themes', self.settings['THEME'])
        self.theme_staticpath = os.path.join(self.themepath, 'static')
        self.theme_templatepath = os.path.join(self.themepath, 'templates')
        self.dest_themepath = os.path.join(self.destpath, self.settings['THEME'])

        
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
        if (self.output_folder_ready(self.output_root)):
            for folder in self.settings['STATIC']:
                staticwriter(os.path.abspath(os.path.expanduser(folder)),
                             os.path.abspath(os.path.expanduser(self.destpath)))
            # Copying Theme files!
            staticwriter(os.path.abspath(os.path.expanduser(self.theme_staticpath)),
                         os.path.abspath(os.path.expanduser(self.dest_themepath)))

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
        comiclist = csvreader(os.path.abspath(os.path.expanduser(self.settings['COMIC_CSV'])))
        
        #write comics!
        defaultwriter(comiclist, self.theme_templatepath, self.output_root, self.settings)
        print "Done"


def main():
    settings = get_settings()
    comatic = Comatic(settings)
    comatic.init_path()
    comatic.run()


if __name__ == "__main__":
    main()
