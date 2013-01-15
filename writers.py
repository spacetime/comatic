import os
import shutil, errno
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

def staticwriter(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def defaultwriter(comiclist, theme_path, output_path, settings):
    template_strip_abspath = os.path.abspath(os.path.expanduser(os.path.join(theme_path,'strip.html')))
    template_author_abspath = os.path.abspath(os.path.expanduser(os.path.join(theme_path,'author.html')))
    template_archives_abspath = os.path.abspath(os.path.expanduser(os.path.join(theme_path,'archives.html')))

    jinja_env = Environment(loader=FileSystemLoader(theme_path),
                          trim_blocks=True)
    #print comic_map
    #format of comic strip: {number, timestamp, extrainfo, title, author, alttext}
    #Write Comics
    laststrip = comiclist[-1]
    lastnumber = int(laststrip[0])
    for comicstrip in comiclist:
        comicnumber = int(comicstrip[0])
        timestamp = comicstrip[1]
        description = comicstrip[2]
        title = comicstrip[3]
        author = comicstrip[4]
        alternate = comicstrip[5]
        comicfile = jinja_env.get_template('comicstrip.html').render(
                    sitetitle = settings['TITLE'],
                    number = comicnumber, 
                    comictitle = title,
                    limit = lastnumber,
                    alttext = alternate,
                    )
        strip_dir = os.path.join(output_path,'%d' % comicnumber)
        os.makedirs(strip_dir)
        print strip_dir
        comic_strip_path = os.path.join(strip_dir,'index.html')
        file_writer = open(comic_strip_path,'w')
        file_writer.write(comicfile)
        file_writer.close()
    #write index
    #write authors page
    #write archives page
    pass

