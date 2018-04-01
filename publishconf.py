#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# changed
#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-XXXXX-Y"

# Uncomment this to use extension-less urls on your hosting provider
# Aerobatic automtically redirects /foo.html to /foo, so this saves
# a redirect round-trip
ARTICLE_URL = '{category}/{slug}'
CATEGORY_URL = '{category}/'