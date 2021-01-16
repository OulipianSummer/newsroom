# From this tutorial
# https://learndjango.com/tutorials/django-markdown-tutorial

# blog/templatetags/markdown_extras.py
from django import template
from django.template.defaultfilters import stringfilter
from bs4 import BeautifulSoup
import hashlib

import markdown as md

register = template.Library()

# Converts markdown to HTML elements
@register.filter(name='markdown')
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

# Strips markdown syntax from an article and sends back plain text for use as a sneak peak
@register.filter(name='plaintext')
@stringfilter
def plaintext(value):
    return ''.join(BeautifulSoup(markdown(value), 'html5lib').findAll(text=True))

# An MD5 hashing tag that provides a hashed value to gravatar
@register.filter(name='md5')
@stringfilter
def md5_string(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()

# Truncates an article's text to the first 150 characters, for card text
@register.filter(name='lead')
@stringfilter
def four_line_lead(value):
    return value[:150] + "..."