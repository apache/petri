#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

import sys
import os


AUTHOR = u'Petri Community'
SITENAME = u'Apache Petri'
SITEURL = ''
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
SITEURL = 'https://petri.apache.org'

# Save pages using full directory preservation
PAGES_PATHS = [ 'content' ]
#PATH_METADATA= '(?P<path_no_ext>.*)\..*'
#PAGE_SAVE_AS= '{path_no_ext}.html'
#PAGE_URL= '{path_no_ext}.html'
SLUGIFY_SOURCE = 'basename'
PAGE_SAVE_AS = '{slug}.html'

# We don't use articles, but we don't want pelican to think
# that content/ contains articles.
ARTICLE_PATHS = [ 'articles' ]

# Disable these pages
ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Disable feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
#PLUGINS = ['toc']
TOC_HEADERS = r"h[1-6]"

# Unused links
LINKS = ( )
SOCIAL = ( )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
