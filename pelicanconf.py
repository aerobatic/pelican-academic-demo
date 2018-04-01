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
    'md-metayaml',
    'render_math',
    'share_post',
    'liquid_tags.youtube'
]

PLUGIN_PATHS=['plugins']

JINJA_ENVIRONMENT = {
    'trim_blocks': True,
    'lstrip_blocks': True,
    'extensions': ['jinja2.ext.do']
}

# Simple custom jinja filter for date formatting
JINJA_FILTERS = {
    'datetimeformat': lambda value, format : value.strftime(format)
}

# Set this so autoreload will detect changes to templates
STATIC_PATHS = ['images', 'css', 'js']

# Automatically assign the category of an article
# based on the sub-folder of content
USE_FOLDER_AS_CATEGORY = True

# CATEGORY_URL = '{category}/index.html'
# CATEGORY_SAVE_AS = '{category}/index.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
INDEX_SAVE_AS = 'index.html'

LOAD_CONTENT_CACHE = False
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

THEME_TEMPLATES_OVERRIDES = ['templates']


ARTICLE_EXCLUDES = ['content/widgets']

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

# The PROFILE_METADATA is used both for JSON-LD metadata on
# the site homepage and for the profile jinja2 component.
# At a minimum you should specify "name". Beyond that, share
# as little or as much as you wish. The full set of possible properties
# can be found at: http://schema.org/Person in the JSON-LD tab.
PROFILE_METADATA = {
    'name': 'Albus Dumbledore',
    'worksFor': {
        'name': "Hogwart\'s School of Magic",
        'location': ''
    },
    'jobTitle': 'Headmaster, Professor of Transfiguration'
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = 'atom.xml'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
