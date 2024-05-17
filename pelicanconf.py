
# Basic information about the site.
SITENAME = 'Apache Petri'
SITEDESC = 'Assists external project communities interested in becoming an Apache project learn how The ASF works and its views on how to build a healthy community'
SITEDOMAIN = 'petri.apache.org'
SITEURL = 'https://petri.apache.org'
SITELOGO = 'https://petri.apache.org/images/logo.png'
SITEREPOSITORY = 'https://github.com/apache/petri/blob/master/content/'
CURRENTYEAR = 2024
TRADEMARKS = 'Apache, the Apache feather logo, and Petri are trademarks or registered trademarks'
TIMEZONE = 'UTC'
# Theme includes templates and possibly static files
THEME = 'theme/apache'
# Specify location of plugins, and which to use
PLUGIN_PATHS = [ 'theme/plugins',  ]
PLUGINS = [ 'toc2', 'gfm',  ]
# All content is located at '.' (aka content/ )
PAGE_PATHS = [ '.' ]
STATIC_PATHS = [ '.',  ]
# Where to place/link generated pages

PATH_METADATA = '(?P<path_no_ext>.*)\\..*'

PAGE_SAVE_AS = '{path_no_ext}.html'
# Don't try to translate
PAGE_TRANSLATION_ID = None
# Disable unused Pelican features
# N.B. These features are currently unsupported, see https://github.com/apache/infrastructure-pelican/issues/49
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
# Disable articles by pointing to a (should-be-absent) subdir
ARTICLE_PATHS = [ 'blog' ]
# needed to create blogs page
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# Disable all processing of .html files
READERS = { 'html': None, }








