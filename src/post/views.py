from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Photo

# Create your views here.
from django.views.generic import DetailView


class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = '/Users/laura/django/d_venv/src/post/templates/post/post_detail.html'
    # success_url ='/restaurants/'
    login_url='/login/'
    def get_context_data(self,*args,**kwargs):
        context = super(PostDetailView,self).get_context_data(*args,**kwargs)
        restaurant = self.get_object().restaurant
        context['title'] = f'Update Restaurant: {restaurant}'

        return context

    def get_queryset(self):
        # return Photo.objects.filter(owner=self.request.user)
        return Photo.objects.all()