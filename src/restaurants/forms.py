from django import forms

from .models import RestaurantLocation,Photo
from .validators import validate_category
from django.forms import inlineformset_factory


class RestaurantCreateForm(forms.Form):
        name            = forms.CharField()
        location        = forms.CharField(required=False)
        category        = forms.CharField(required=False)

    # def clean_name(self):
    #     name= self.cleaned_data.get('name')
    #     if name =="Hello":
    #         raise forms.ValidationError("Not a valid name")
    #     return name

class RestaurantLocationCreateForm(forms.ModelForm):
    # email               = forms.EmailField()
    # category            =forms.CharField(required=False,validators = [validate_category])
    class Meta:
        model =RestaurantLocation
        fields =[
            'name',
            'location',
            'address',
            'category',
            'cover_image',
            'slug',
        ]
    def clean_name(self):
        name= self.cleaned_data.get('name')
        if name =="Hello":
            raise forms.ValidationError("Not a valid name")
        return name
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if ".edu" in email:
    #         raise forms.ValidationError("We don't accept edu emails.")
    #     return email

# multi image
class MultiImageForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = [
            'title',
            'image',
            'caption'
        ]

RestaurantFormSet = inlineformset_factory(
    RestaurantLocation,
    Photo,
    form=MultiImageForm,
    extra=1,
    can_delete=False,
    can_order=False
)
