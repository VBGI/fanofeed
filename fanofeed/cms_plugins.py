# -*- coding: utf-8 -*-


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import FanoFeed
from django.utils.translation import ugettext_lazy as _


class FanoFeedParser(CMSPluginBase):
    model = FanoFeed
    name = _(u"Новости РАН")
    render_template = "cms/plugins/fanoplugin.html"
    text_enabled = True
    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(FanoFeedParser)



