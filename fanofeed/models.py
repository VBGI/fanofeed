# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from .settings import FEED_URLS


class NewsFeeder(CMSPlugin):
    name = models.CharField(max_length=1, default='R',
                            choices=map(lambda x: (x[2], x[1]), FEED_URLS))
