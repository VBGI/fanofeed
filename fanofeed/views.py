# -*- coding: utf-8 -*-
# Create your views here.

from django.template.loader import render_to_string
from django.http import HttpResponse
import feedparser
from django.views.decorators.cache import cache_page
from .settings import FANO_RSS_URL, NEWS_NUMBER
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


# Parse news once per half-a-day
@cache_page(43200)
def fano_parser(request):
    objs = []
    try:
        data = feedparser.parse(FANO_RSS_URL)
        for item in data['entries']:
            objs.append({'title': strip_tags(item['title']),
                         'published': feedparser._parse_date(item['published']),
                         'link': item['link']})
            objs.sort(key=lambda x: x['published'])
            objs = objs[::-1]
    except:  # be quiet, if something goes wrong...
        objs = []  # clear objs in any case...
    if objs:
        return HttpResponse(render_to_string('fanorss.html', {'objs':
                                                              objs[:NEWS_NUMBER]}),
                           content_type='text/plain')
    else:
        return HttpResponse('', content_type='text/plain')
