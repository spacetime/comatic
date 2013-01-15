comatic
=======

comatic is a python based Static webcomic generator.
It is based on the xkcd style of comic management for now.

# Dependencies 
* Jinja2
* Python 2.x

It will power hopefully my webcomic that used to run on comicpress one day. :')

This is a weekend hack. I took special care to throw away every good coding practice.
If anyone else is interested in using it, I'll clean it up!

# Using comatic
* Set up your configuration as settings.py
* The list of comics is picked up from a CSV. This must be the worst method you've heard of,
 but I considered ReStructuredText/Markdown but this seemed the best way to go forward to me.
* Note that comatic only supports xkcd style URLs in series. For instance.
  your-comic-site.com/1
  your-comic-site.com/2
  your-comic-site.com/3
  and so on.
* The CSV must look like this: number,timestamp,title,author,image path,alternate text,description

# Finished Stuff
* the comic strip part

# TODO
* Author pages
* Extra pages
* Disqus support (can be added in theme)
* Google Analytics (can be added in theme)
* User settings file <- urgent
