from django.db import models
from django.conf import settings

from restaurants.models import RestaurantLocation
from django.core.urlresolvers import reverse

# Create your models here.

class Photo(models.Model):
    # associations
    owner           = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant      = models.ForeignKey(RestaurantLocation)

    title           = models.CharField("照片標題",max_length=100,default='')
    image           = models.ImageField("上傳照片",upload_to='static/media/')
    caption         = models.TextField("照片說明",max_length=250,blank=True,default='')
    timestamp       = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    #
    # def get_absolute_url(self):
    #     # return f'/restaurants/{self.slug}'
    #     return reverse('restaurants:detail',kwargs={'owner':self.ow})
    #
    def get_absolute_url(self):
        return reverse('restaurants:detail',kwargs={'slug':self.restaurant.slug})

    def get_absolute_url_detail(self):
        # return f'/restaurants/{self.slug}'
        return reverse('post:detail', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['-timestamp']