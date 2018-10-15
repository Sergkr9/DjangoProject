"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import include, url

import DjangPr.views

urlpatterns = [
    url (r'^$', DjangPr.views.index, name ='index'),
    url (r'^home$', DjangPr.views.index, name ='home')
    ]