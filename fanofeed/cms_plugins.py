# -*- coding: utf-8 -*-


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import NewsFeeder
from django.utils.translation import ugettext_lazy as _


class NewsFeedParser(CMSPluginBase):
    model = NewsFeeder
    name = _(u"Новости РАН")
    render_template = "cms/plugins/newsfeedplugin.html"
    text_enabled = True
    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(NewsFeedParser)



