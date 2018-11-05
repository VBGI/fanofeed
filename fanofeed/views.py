# -*- coding: utf-8 -*-
# Create your views here.

from django.template.loader import render_to_string
from django.http import HttpResponse
import feedparser
from django.views.decorators.cache import cache_page
from .settings import FEED_URLS
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import urllib

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
@cache_page(FEED_URLS[0][3])
def ras_parser(request):
    objs = []
    try:
        data = feedparser.parse(FEED_URLS[0][0])
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
                                                              objs[:FEED_URLS[0][-1]]}),
                           content_type='text/plain')
    else:
        return HttpResponse('', content_type='text/plain')


@cache_page(FEED_URLS[1][3])
def minobr_parser(request):
    soup = BeautifulSoup(urllib.urlopen(FEED_URLS[1][0]).read())
    news = soup.find('a', attrs={'class': 'news-list__title'})
    

