# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save,post_save

from .utils import unique_slug_generator
from .validators import validate_category

from django.core.urlresolvers import reverse

# Create your models here.

from django.contrib import admin

User = settings.AUTH_USER_MODEL

class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                    Q(name__icontains=query)|
                    Q(location__icontains = query)|
                    Q(location__iexact = query)|
                    Q(category__icontains = query)|
                    Q(category__iexact = query)|
                    Q(item__name__icontains = query)|
                    Q(item__contents__icontains = query)

                     ).distinct()
        return self

class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using = self._db)
    def search(self, query):
        return self.get_queryset().search(query)


class RestaurantLocation(models.Model):
    owner           = models.ForeignKey(User) # class_instance.model_set.all()
    name            = models.CharField("店名",max_length=120)
    location        = models.CharField("地區",max_length=120, null=True, blank=True)
    address         = models.CharField("地址", max_length=120,null=True, blank=True)
    category        = models.CharField("種類",max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp       = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    cover_image     = models.ImageField("封面",upload_to='static/media/', null=True, blank=True)
    slug            = models.SlugField(null=True, blank=True)



    objects = RestaurantLocationManager() #add Model.objects.all()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f'/restaurants/{self.slug}'
        return reverse('restaurants:detail',kwargs={'slug':self.slug})

    def get_absolute_url_edit(self):
        # return f'/restaurants/{self.slug}'
        return reverse('restaurants:update-detail',kwargs={'slug':self.slug})

    def get_absolute_url_all(self):
        # return f'/restaurants/{self.slug}'
        return reverse('restaurants:detail-all',kwargs={'slug':self.slug})

    def get_absolute_url_post(self):
        return reverse('restaurants:add-post',kwargs={'slug':self.slug})

    def get_id(self):
        return self.id

    @property
    def title(self):
        return self.name #object.title

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    instance.category = instance.category.capitalize()
    print("saving..")
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
    print("saved")
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

# class Photo(models.Model):
#     # associations
#     owner           = models.ForeignKey(settings.AUTH_USER_MODEL)
#     restaurant      = models.ForeignKey(RestaurantLocation)
#
#     title           = models.CharField("照片標題",max_length=100,default='')
#     image           = models.ImageField("上傳照片",upload_to='static/media/')
#     caption         = models.CharField("照片說明",max_length=250,blank=True,default='')
#     timestamp       = models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return self.title
#
#
#     def get_absolute_url(self):
#         return reverse('restaurants:detail',kwargs={'slug':self.restaurant.slug})
#
#     class Meta:
#         ordering = ['-timestamp']




pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)
