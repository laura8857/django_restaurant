from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView, UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm,RestaurantLocationCreateForm,RestaurantFormSet
import random

# from django.conf import settings
# from django.contrib.gis.maps.google.gmap import GoogleMap
# from django.contrib.gis.maps.google.overlays import GMarker, GEvent
# from django.shortcuts import render_to_response


# @login_required()
# import random

# Create your views here.
# function based views

# def home(request):
#     html_var="f strings"
#     html_=f"""
#     <!DOCTYPE html>
#     <html>
#       <head>
#         <meta charset="utf-8">
#         <title></title>
#       </head>
#       <body>
#         <h1>hello wolrd</h1>
#         <p>This is {html_var} in the world</p>
#       </body>
#     </html>
#
#     """
#
#     return HttpResponse(html_)
#     # return render(request, "home.html",{})#response

# def home(request):
#     num = random.randint(0,100000)
#     x_list = [num,random.randint(0,100000),random.randint(0,100000)]
#     context = {
#         "html_var":"context variable",
#         "num":num,
#         "bool_item":False,
#         "x_list":x_list
#     }
#     return render(request,"home.html",context)
#
# def about(request):
#     context={}
#     return render(request,"about.html",context)
#
# def contact(request):
#     context={}
#     return render(request,"contact.html",context)

# class ContactView(View):
#     def get(self,request,*args,**kwargs):
#         context={}
#         return render(request,"contact.html",context)
#
    # def post(self,request,*args,**kwargs):
    #     context={}
    #     return render(request,"contact.html",context)
    #
    # def put(self,request,*args,**kwargs):
    #     context={}
    #     return render(request,"contact.html",context)

# class HomeView(TemplateView):
#     template_name = "home.html"
#
#     def get_context_data(self,*arg,**kwargs):
#         context =super(HomeView,self).get_context_data(*arg,**kwargs)
#         num = random.randint(0,100000)
#         x_list = [num,random.randint(0,100000),random.randint(0,100000)]
#         context = {
#             "html_var":"context variable",
#             "num":num,
#             "bool_item":False,
#             "x_list":x_list
#         }
#         print(context)
#         return context


# class AboutView(TemplateView):
#     template_name = "about.html"
#
#
# class ContactView(TemplateView):
#     template_name = "contact.html"

# def restaurant_createview(request):
#     form = RestaurantLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         form.save()
#         if request.user.is_authenticated():
#             instance = form.save(commit = False)
#             instance.owner = request.user
#             instance.save()
#             # obj = RestaurantLocation.objects.create(
#             #     name = form.cleaned_data.get("name"),
#             #     location = form.cleaned_data.get("location"),
#             #     category = form.cleaned_data.get("category"),
#             # )
#             return HttpResponseRedirect("/restaurants/")
#         else:
#             return HttpResponse("/login/")
#     else:
#         form = RestaurantLocationCreateForm()
#     if form.errors:
#         erros = form.errors
#
#     template_name='/Users/laura/django/d_venv/src/restaurants/templates/restaurants/form.html'
#     context={
#         'form':form,
#         'errors':errors
#     }
#     return render(request,template_name,context)
# def restaurant_listview(request):
#     template_name='/Users/laura/django/d_venv/src/restaurants/templates/restaurants/restaurant_list.html'
#     queryset= RestaurantLocation.objects.all()
#     context={
#         "object_list":queryset
#     }
#     return render(request,template_name,context)
#
#
# def restaurant_detailview(request,slug):
#     template_name='/Users/laura/django/d_venv/src/restaurants/templates/restaurants/restaurantolocation_detail.html'
#     obj= RestaurantLocation.objects.get(slug=slug)
#     context={
#         "object":obj
#     }
#     return render(request,template_name,context)

class RestaurantListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)

    # def get_queryset(self):
    #     # print(self.kwargs)
    #     slug = self.kwargs.get("slug")
    #     if slug:
    #         queryset= RestaurantLocation.objects.filter(
    #             Q(category__iexact=slug) |
    #             Q(category__icontains=slug)
    #         )
    #     else:
    #         queryset= RestaurantLocation.objects.all()
    #     return queryset

class RestaurantDetailView(LoginRequiredMixin,DetailView):
    # form_class = RestaurantLocationCreateForm

    # success_url ='/restaurants/'
    login_url='/login/'
    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'

        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)

class RestaurantDetailViewAll(LoginRequiredMixin,DetailView):
    template_name = '/Users/laura/django/d_venv/src/restaurants/templates/restaurants/restaurantlocation_detail_all.html'

    # success_url ='/restaurants/'
    login_url='/login/'
    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantDetailViewAll,self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'

        return context

    def get_queryset(self):
        return RestaurantLocation.objects.all()


    # def get_context_data(self,*args,**kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #
    #     return context

    # def get_object(self,*args,**kwargs):
    #     rest_id = self.kwargs.get("rest_id")
    #     obj = get_object_or_404(RestaurantLocation,id = rest_id ) #pk = rest_id
    #     return obj


# class AsianRestaurantListView(ListView):
#     queryset= RestaurantLocation.objects.filter(category__iexact="新加坡")
#     template_name='/Users/laura/django/d_venv/src/restaurants/templates/restaurants/restaurant_list.html'

class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    # success_url ='/restaurants/'
    login_url='/login/'

    def form_valid(self,form):
        instance = form.save(commit = False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantCreateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Restaurant'

        if self.request.method == 'POST':
            context['RestaurantFormSet'] = RestaurantFormSet(self.request.POST)
        else:
            context['RestaurantFormSet'] = RestaurantFormSet()

        return context


class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'
    # success_url ='/restaurants/'
    login_url='/login/'


    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'

        if self.request.method == 'POST':
            context['RestaurantFormSet'] = RestaurantFormSet(self.request.POST)
        else:
            context['RestaurantFormSet'] = RestaurantFormSet()

        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)


class RestaurantGoogleMapView(LoginRequiredMixin,ListView):
    template_name = '/Users/laura/django/d_venv/src/templates/google_map.html'
    def get_queryset(self):
        num_obj = len(RestaurantLocation.objects.all()) +1
        if num_obj >0:
            random_id = random.randint(1,num_obj)
            return RestaurantLocation.objects.filter(id=random_id)
        else:
            RestaurantLocation.objects.all()
