# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
    RestaurantDetailViewAll,
    RestaurantPostView

)

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(),name='lists'),
    url(r'^create/$', RestaurantCreateView.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name = 'detail'),
    url(r'^(?P<slug>[\w-]+)/update$', RestaurantUpdateView.as_view(),name = 'update-detail'),
    url(r'^(?P<slug>[\w-]+)/all$', RestaurantDetailViewAll.as_view(),name = 'detail-all'),
    url(r'^(?P<slug>[\w-]+)/add_post$', RestaurantPostView.as_view(),name = 'add-post'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(),name = 'edit')
]
