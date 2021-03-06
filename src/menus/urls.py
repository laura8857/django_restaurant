# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView

)

urlpatterns = [
    url(r'^$', ItemListView.as_view(),name='lists'),
    url(r'^create/$', ItemCreateView.as_view(),name='create'),
    # url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(),name = 'detail'),
    url(r'^(?P<pk>[\w-]+)/$', ItemUpdateView.as_view(),name = 'detail'),
    # url(r'^(?P<pk>\d+)/edit$', ItemUpdateView.as_view(),name = 'edit')
]
