from django.shortcuts import render

from django.views.generic import View,ListView, DetailView, CreateView, UpdateView
from .models import Item

from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(View):
    """docstring for HomeView"""
    def get(self,request,*args,**keargs):
        if not request.user.is_authenticated():
            return render(request,"home.html",{})

        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        # print(is_following_user_ids)
        qs = Item.objects.filter(user__id__in = is_following_user_ids,public=True)
        # print(qs)

        return render(request,"menus/home-feed.html",{"object_list":qs})


class ItemListView(LoginRequiredMixin,ListView):
    """docstring for ItemListView"""
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin,DetailView):
    """docstring for ItemListView"""
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin,CreateView):
    """docstring for ItemListView"""
    template_name = 'form.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self,*args,**kwargs):
        context = super(ItemCreateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Create Item'
        return context

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)




class ItemUpdateView(LoginRequiredMixin,UpdateView):
    """docstring for ItemListView"""
    template_name = 'menus/detail-update.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self,*args,**kwargs):
        context = super(ItemUpdateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Update Item'

        return context

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
