from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.

from .utils import code_generator
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    """docstring for ProfileManager"""
    def toggle_follow(self,request_user,username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact = username_to_toggle)
        user= request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_ , is_following

class Profile(models.Model):
    """docstring for Profile"""
    user            = models.OneToOneField(User)
    followers       = models.ManyToManyField(User, related_name = 'is_following', blank = 'True')
    # following       = models.ManyToManyField(User, related_name = 'followings', blank = 'True')
    activation_key  = models.CharField(max_length =120,blank = True,null = True)
    activated       = models.BooleanField(default = False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)

    objects =ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        print("Activation")
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate',kwargs={'code':self.activation_key})
            # path_ ='http://laurahu8857.pythonanywhere.com'+path_
            path_='http://127.0.0.1:8000'+path_
            subject = 'Activated Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activated your account here:{path_}'
            recipient_list = [self.user.email]
            html_message = f'<p>Activated your account here:<a href ="{path_}">{path_}</a></p>'
            sent_mail =send_mail(
                            subject,
                            message,
                            from_email,
                            recipient_list,
                            fail_silently=False,
                            html_message=html_message)

            return sent_mail

def post_save_user_receiver(sender,instance,created,*args,**kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user = instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0] #新user follow第一個user
        print(default_user_profile)
        default_user_profile.followers.add(instance)
        # default_user_profile.followers.remove(instance)
        profile.followers.add(default_user_profile.user)  #新的user被default 2 user follow
        profile.followers.add(2)


post_save.connect(post_save_user_receiver ,sender = User)
