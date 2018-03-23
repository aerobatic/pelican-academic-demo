#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# from __future__ import unicode_literals
# from pelican.readers import Markdown
# import markdown

AUTHOR = u'David Von Lehman'
SITENAME = u'PELICAN ACADEMIC'
SITEURL = '/'

THEME = 'pelican-academic'
PATH = 'content'

PLUGINS = [
    'frontmark'
]

# Set this so autoreload will detect changes to templates
STATIC_PATHS = ['images', 'css', 'js']

LOAD_CONTENT_CACHE = False
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

THEME_TEMPLATES_OVERRIDES = ['templates']


ARTICLE_EXCLUDES = ['content/widgets']

# PLUGIN_PATHS = ['themes/pelican-academic/plugins']
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['jinja2content']

# DIRECT_TEMPLATES = ['index']
# EXTRA_TEMPLATES_PATHS = ['templates']
# TEMPLATE_PAGES = {'pages/index.html': 'index.html'}

# def markdown_convert(input):
#     print input
#     return 'FOOOOO' + markdown.markdown(input)
#
# JINJA_FILTERS = {
#     'markdown': markdown_convert,
#     'upper': lambda input:input.upper()
# }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = 'atom.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
