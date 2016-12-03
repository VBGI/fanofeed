# -*- coding: utf-8 -*-
# Create your views here.

from django.template.loader import render_to_string
from django.http import HttpResponse
import feedparser
from django.views.decorators.cache import cache_page
from .settings import FANO_RSS_URL


# Parse news once per half-a-day
@cache_page(43200)
def fano_parser(request):
    objs = []
    try:
        data = feedparser.parse(FANO_RSS_URL)
        for item in data['entries']:
            objs.append({'title': item['title_detail']['value'],
                         'link': item['link']})
    except:  # If something goes wrong, don't cry and be quiet...
        objs = []  # clear objs in any case...
    if objs:
        return HttpResponse(render_to_string('fanorss.html', {'objs': objs}),
                            content_type='text/plain')
    else:
        return HttpResponse('', content_type='text/plain')
