from django.conf.urls import *

from .views import minobr_parser, ras_parser


urlpatterns = patterns('',
                       url(r'^0/', ras_parser, name='ras_parser'),
                       url(r'^1/', minobr_parser, name='minobr_parser')
                       )
