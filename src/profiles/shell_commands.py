from django.contrib.auth import get_user_model

User = get_user_model

random_ = Users.objects.last()

# my followers
random_.profile.followers.all()

#  who i follow
random_.is_following.all()
