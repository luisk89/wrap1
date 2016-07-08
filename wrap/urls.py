from django.conf.urls import patterns,url
from django.views.generic.base import TemplateView

__author__ = 'Luisk'

urlpatterns = patterns('',
                       # Examples:
                       url(r'^/', TemplateView.as_view(template_name="index.html")),
                       )