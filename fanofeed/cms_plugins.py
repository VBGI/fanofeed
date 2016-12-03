# -*- coding: utf-8 -*-


from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _


class FanoFeedParser(CMSPluginBase):
    model=CMSPlugin
    name = _(u"Новости ФАНО")
    render_template = "cms/plugins/fanoplugin.html"
    text_enabled = True
    def render(self, context, instance, placeholder):
        return context


plugin_pool.register_plugin(FanoFeedParser)



