# -*- coding: utf-8 -*-
"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# from restaurants.views import HomeView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView

from profiles.views import ProfileFollowToggle,RegisterView,activate_user_view
from menus.views import HomeView
from restaurants import views
from restaurants.views import RestaurantGoogleMapView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^register/$', RegisterView.as_view(),name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view,name = "activate"),
    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^logout/$', LogoutView.as_view(),name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),name = 'about'),
    url(r'^restaurants/', include('restaurants.urls',namespace='restaurants')),
    url(r'^googlemap/$', RestaurantGoogleMapView.as_view(),name='googlemap'),
    url(r'^post/', include('post.urls',namespace='post')),
    url(r'^items/', include('menus.urls',namespace='menus')),
    url(r'^u/', include('profiles.urls',namespace='profile')),
    # url(r'^restaurants/$', RestaurantListView.as_view(),name='restaurants'),
    # url(r'^restaurants/create/$', restaurant_createview),#RestaurantCreateView.as_view()),
    # url(r'^restaurants/create/$', RestaurantCreateView.as_view(),name='restaurants-create'),
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name = 'restaurant-detail'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
