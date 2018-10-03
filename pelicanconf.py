#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Bryce Caine'
SITENAME = "Bryce Caine's Blog"
SITEURL = 'https://www.brycecaine.com'

PATH = 'content'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
'''
LINKS = (('Python', 'http://python.org/'),
         ('Pelican', 'http://getpelican.com/'),)
'''

# Social widget
SOCIAL = (('github', 'https://github.com/brycecaine'),
          ('linkedin', 'https://linkedin.com/brycecaine'),
          ('twitter', 'https://twitter.com/brycecaine'),
          ('google', 'https://plus.google.com/117024465923249915159'),
          ('envelope', 'mailto:brycecaine@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ------------------------
# Bryce add
DISQUS_SITENAME = 'brycecaine'
# Works with disqus
# THEME = "themes/aboutwilson"
THEME = "themes/Flex"
SITETITLE = 'Bryce Caine'
SITESUBTITLE = 'Dad, Data, Developer'
SITEDESCRIPTION = 'Blog'
SITELOGO = SITEURL + '/images/brycecaine.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

# BROWSER_COLOR = '#ABC'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = datetime.now().year

MAIN_MENU = True
MENUITEMS = (('Categories', SITEURL + '/categories'),
             ('Tags', SITEURL + '/tags'),
             ('Archive', SITEURL + '/archives'),)

ADD_THIS_ID = 'ra-5b594f00d814fcaa'

GOOGLE_ANALYTICS = 'UA-55396444-1'
GOOGLE_TAG_MANAGER = 'GTM-5X725WK'
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'design': 6, 'rumid': 1234 }

ARTICLE_URL = '{slug}'
PAGE_URL = 'pages/{slug}'
