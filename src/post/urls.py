from django.conf.urls import url


from .views import (
    PostDetailView
#
)
#
urlpatterns = [
#     url(r'^$', ItemListView.as_view(),name='lists'),
#     url(r'^create/$', ItemCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(),name = 'detail'),
#     # url(r'^(?P<pk>\d+)/edit$', ItemUpdateView.as_view(),name = 'edit')
]
