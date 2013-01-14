import shutil, errno
from jinja2 import Template

def staticwriter(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def defaultwriter(theme,output):
    #TODO
    pass
