# Apache Theme

## Page Templates

1. base.html - there is only one page type.

Change the base page as necessary and add new page types as required.

See [Web Developer](../../../DEVELOPER.md) for framework and other information.

## Pelican Variables set in [pelicanconf.py](../../../pelicanconf.py)

~~~python
SITENAME = u'Apache Petri'
SITEDOMAIN = 'petri.apache.org'
SITEURL = 'https://petri.apache.org'
SITELOGO = 'https://petri.apache.org/images/logo.png'
SITEDESC = u'<pmc desc>'
SITEREPOSITORY = 'https://github.com/apache/petri/blob/master/content/pages/'
TRADEMARKS = u'Apache, the Apache feather logo, and Petri are trademarks or registered trademarks'
CURRENTYEAR = date.today().year
~~~
