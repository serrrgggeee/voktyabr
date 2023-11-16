from django import forms
from django.contrib.auth.models import User
from enumeration.models import Enumeration
from organisations.models import Organisation
from place.models import Place


class PhotoAploadForm(forms.Form):
    TYPE_CHOICES = (
        ('', '------'),
        ('nature', 'Природа'),
        ('soc', 'Общество'),
        ('info', 'Информация'),
    )
    file = forms.FileField(widget=forms.FileInput(attrs={'multiple': ''}))
    place = forms.ModelChoiceField(required=False, queryset=Place.objects.all())
    organisation = forms.ModelChoiceField(required=False, queryset=Organisation.objects.all())
    type_photo = forms.ChoiceField(required=False,choices=[("------", ""),("place", "place"),
                                         ("organisation", "organisation")])
    user = forms.ModelChoiceField(required=True, queryset=User.objects.all())
    photo_type = forms.ChoiceField(required=False, choices=TYPE_CHOICES)


class FileAploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput())
    place = forms.ModelChoiceField(required=False, queryset=Place.objects.all())
    parent = forms.ModelChoiceField(required=False, queryset=Enumeration.objects.all())

