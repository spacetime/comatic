settings = {
    'AUTHOR': u'Rishab Arora',
    'SITENAME' : u'Arthik Tangi',
    'SITEURL' : 'http://www.arthiktangi.com',
    'TITLE' : u'Arthik Tangi: Random thoughts from randomized minds',
    
    'TIMEZONE' : 'Asia/Kolkata',
    
    'GOOGLE_ANALYTICS' : "UA-xxxxx-1",
    'DISQUS_ID' : 'xxxx',
    
    'COMIC_CSV' : 'contents/list.csv',
    'STATIC' : {'images'},
    'OUTPUT_PATH' : 'output',
    
    'EXTRA_MENU' : {
        #('Archives','/archives.html'),
        },

    'THEME': 'arthiktangi',
    'FOOTER': """
 This work is licensed under a Creative Commons Attribution-NonCommercial 2.5 License. 
"""
}

def get_settings():
    return settings
